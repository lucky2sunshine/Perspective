import re
from toxic import Perspectiveapi

page_text = str(open('./立陶宛.html', 'r').read())
pattern = r'<h3 data-v-11d91d52="">(.+)</h3>'
comments = re.findall(pattern, page_text)
comments = [comment.split('<')[0] for comment in comments]
print(comments)
print(len(comments))

Perspectiveapi.check_from_list(comments)


