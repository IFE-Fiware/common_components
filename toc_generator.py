import re
import argparse
from pathlib import Path

def generate_anchor(text):
    """Generate GitHub-style anchor from header text"""
    # Convert to lowercase and replace spaces/special chars with hyphens
    anchor = re.sub(r'[^\w\s-]', '', text.lower())
    anchor = re.sub(r'[-\s]+', '-', anchor)
    return anchor.strip('-')

def extract_headers(markdown_content):
    """Extract headers from markdown content, ignoring headers inside code blocks"""
    headers = []
    lines = markdown_content.split('\n')
    
    in_code_block = False
    code_fence_pattern = re.compile(r'^```')
    
    for line_num, line in enumerate(lines, 1):
        stripped_line = line.strip()
        
        # Check for code fence (``` or ~~~)
        if code_fence_pattern.match(stripped_line) or stripped_line.startswith('~~~'):
            in_code_block = not in_code_block
            continue
        
        # Skip processing if we're inside a code block
        if in_code_block:
            continue
        
        # Check for indented code blocks (4+ spaces or 1+ tabs)
        if line.startswith('    ') or line.startswith('\t'):
            continue
        
        # Match ATX-style headers (# ## ### etc.)
        match = re.match(r'^(#{1,6})\s+(.+)', stripped_line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            anchor = generate_anchor(title)
            headers.append({
                'level': level,
                'title': title,
                'anchor': anchor,
                'line': line_num
            })
    
    return headers

def generate_toc(headers, max_depth=6, style='github'):
    """Generate table of contents from headers"""
    if not headers:
        return "No headers found in the document."
    
    toc_lines = []
    
    if style == 'github':
        # GitHub-style TOC
        for header in headers:
            if header['level'] <= max_depth:
                indent = '  ' * (header['level'] - 1)
                link = f"[{header['title']}](#{header['anchor']})"
                toc_lines.append(f"{indent}- {link}")
    
    elif style == 'numbered':
        # Numbered TOC
        counters = [0] * 6  # Support up to 6 levels
        
        for header in headers:
            if header['level'] <= max_depth:
                level = header['level'] - 1
                counters[level] += 1
                # Reset deeper level counters
                for i in range(level + 1, 6):
                    counters[i] = 0
                
                # Build number string
                number_parts = []
                for i in range(level + 1):
                    if counters[i] > 0:
                        number_parts.append(str(counters[i]))
                
                number = '.'.join(number_parts)
                indent = '  ' * level
                link = f"[{number}. {header['title']}](#{header['anchor']})"
                toc_lines.append(f"{indent}- {link}")
    
    return '\n'.join(toc_lines)

def process_markdown_file(file_path, max_depth=6, style='github', output_file=None):
    """Process a markdown file and generate TOC"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        headers = extract_headers(content)
        toc = generate_toc(headers, max_depth, style)
        
        # Prepare output
        output = f"# Table of Contents\n\n{toc}\n"
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(output)
            print(f"TOC written to {output_file}")
        else:
            print(output)
            
        return toc
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

def insert_toc_in_file(file_path, toc_marker="<!-- TOC -->", max_depth=6, style='github'):
    """Insert or update TOC directly in the markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        headers = extract_headers(content)
        toc = generate_toc(headers, max_depth, style)
        
        if toc_marker in content:
            # Replace existing TOC
            pattern = re.escape(toc_marker) + r'.*?<!-- /TOC -->'
            new_toc = f"{toc_marker}\n{toc}\n<!-- /TOC -->"
            updated_content = re.sub(pattern, new_toc, content, flags=re.DOTALL)
        else:
            # Insert TOC after the first header (usually the main title)
            lines = content.split('\n')
            insert_pos = 1  # Default to after first line
            
            # Find the first header and insert after it
            for i, line in enumerate(lines):
                if line.startswith('#'):
                    # Insert after this header line, skip any empty lines
                    insert_pos = i + 1
                    while insert_pos < len(lines) and lines[insert_pos].strip() == '':
                        insert_pos += 1
                    break
            
            # Create the TOC block
            toc_block = [
                '',
                toc_marker,
                toc,
                '<!-- /TOC -->',
                ''
            ]
            
            # Insert the TOC
            for j, toc_line in enumerate(toc_block):
                lines.insert(insert_pos + j, toc_line)
            
            updated_content = '\n'.join(lines)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"TOC successfully inserted/updated in {file_path}")
        
    except Exception as e:
        print(f"Error updating file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate Table of Contents for Markdown files')
    parser.add_argument('file', help='Path to markdown file')
    parser.add_argument('--max-depth', '-d', type=int, default=6, 
                       help='Maximum header depth to include (default: 6)')
    parser.add_argument('--style', '-s', choices=['github', 'numbered'], default='github',
                       help='TOC style (default: github)')
    parser.add_argument('--output', '-o', help='Output file path (default: print to console)')
    parser.add_argument('--insert', '-i', action='store_true',
                       help='Insert TOC directly into the source file')
    parser.add_argument('--marker', '-m', default='<!-- TOC -->',
                       help='TOC marker for insertion (default: <!-- TOC -->)')
    
    args = parser.parse_args()
    
    if args.insert:
        insert_toc_in_file(args.file, args.marker, args.max_depth, args.style)
    else:
        process_markdown_file(args.file, args.max_depth, args.style, args.output)

if __name__ == "__main__":
    main()