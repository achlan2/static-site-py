import shutil
import sys
import os
from generate_page import generate_page, generate_pages_recursive

def main():

    basepath = '/'
    if sys.argv[0]:
        basepath = sys.argv[0]
    src = 'static'
    destination = 'docs'

    if not os.path.exists(src) or not os.path.isdir(src):
        raise ValueError(f"Source directory '{src}' does not exists or is not a directory")

    os.makedirs(destination, exist_ok=True)

    success_count = 0
    fail_count = 0

    for root, dirs, files in os.walk(src):
        for file in files:
            src_file_path = os.path.join(root, file)

            rel_path = os.path.relpath(src_file_path, src)
            dest_file_path = os.path.join(destination, rel_path)

            try:
                print(f"[COPYING] {src_file_path} -> {dest_file_path}")
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                shutil.copy(src_file_path, dest_file_path)
                print(f"[SUCCESS] {src_file_path}")
                success_count+=1
            except Exception as e:
                print(f"[FAILED] {src_file_path}")
                fail_count +=1

    #generate_page('content/index.md', 'template.html', 'public/index.html')
    generate_pages_recursive('content', 'template.html', destination, basepath)

    print("\n=== COPY SUMMARY ===")
    print(f"✅ Success: {success_count}")
    print(f"❌ Failed : {fail_count}")

if __name__ == '__main__':
    main()
