import os
from jinja2 import Environment, FileSystemLoader
import markdown
import frontmatter

DIR_PATH_PAGES = './pages'
DIR_PATH_POSTS = './posts'

def readfile(path,page):
    # Load Jinja environment 
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('./templates/template.html')

    # Load Markdown content with frontmatter
    with open(f'./{path}/{page}', 'r', encoding='utf-8') as f:
        content = f.read()
        md = frontmatter.loads(content)
        metadata = md.metadata
        html_content = markdown.markdown(md.content)

    # Get a list of all pages
    l=os.listdir(DIR_PATH_PAGES) + os.listdir(DIR_PATH_POSTS)
    li=[x.split('.')[0] for x in l]


    # Render template with data
    return template.render(metadata=metadata, content=html_content, pages=li)

def writefile(output, page):
    # Write output to file
    with open(f'./_site/{page[:-3]}.html', 'w', encoding='utf-8') as f:
        f.write(output)


def main():
    # Loop over every markdown file
    for page in os.listdir(DIR_PATH_PAGES) + os.listdir(DIR_PATH_POSTS):
        # Check in which folder file currently exists
        if os.path.exists(f'./pages/{page}'):
            path = 'pages'
        else:
            path = 'posts'

        output = readfile(path,page)

        writefile(output, page)

main()