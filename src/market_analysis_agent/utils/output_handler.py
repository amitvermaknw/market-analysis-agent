import json
import os
from datetime import datetime

def save_output(result, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    output = result.pydantic.model_dump()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save JSON
    json_file = f'{output_dir}/market_analysis_{timestamp}.json'
    with open(json_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    # Save article as markdown
    md_file = f'{output_dir}/article_{timestamp}.md'
    with open(md_file, 'w') as f:
        f.write(output['article'])

    # Save social media posts as markdown
    social_md_file = f'{output_dir}/social_media_{timestamp}.md'
    with open(social_md_file, 'w') as f:
        f.write("# Social Media Posts\n\n")
        for post in output['social_media_posts']:
            f.write(f"## {post['platform']}\n\n")
            f.write(f"{post['content']}\n\n")
            f.write(f"{'_' * 50}\n\n")
    
    return output, json_file, social_md_file

def print_posts(output):
    for post in output['social_media_posts']:
        print(f"Platform: {post['platform']}")
        print(f"Content: {post['content']}")
        print('_' * 50)