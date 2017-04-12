#!/usr/bin/python
import fontforge
import psMat
import re

# settings
output_html = True
output_css = True
output_list = True
generate_combined_icons = True
generate_splitted_icons = True
generate_slashed_icons = True
generate_stroked_icons = True
workbench_char = 0xe000
start_char = 0xe001
outline_border_weight = 320
horizontal_shifting = 0.7
compress_css = True
icons = {'bookmark':        ['bookmark', 'tr'],
		 'user':            ['user', 'br', False],
		 '_407':            ['cube', 'br'],
		 'camera':          ['camera', 'br'],
		 'tag':             ['tag', 'br'],
		 'tags':            ['tags', 'br'],
		 'uniF1C0':         ['database', 'br', False],
		 'uniF1C1':         ['file-pdf-o', 'br'],
		 '_422':            ['file-word-o', 'br'],
		 '_423':            ['file-excel-o', 'br'],
		 '_424':            ['file-powerpoint-o', 'br'],
		 '_425':            ['file-image-o', 'br'],
		 '_426':            ['file-zip-o', 'br'],
		 '_427':            ['file-audio-o', 'br'],
		 '_428':            ['file-video-o', 'br'],
		 '_429':            ['file-code-o', 'br'],
		 'file':            ['file', 'br'],
		 'file_text':       ['file-text','br', False],
		 'file_text_alt':   ['file-text-o','br'],
		 'envelope_alt':    ['envelope','br'],
		 'link':            ['link','br'],
		 'folder_open_alt': ['folder-open-o', 'br'],
		 'folder_close_alt':['folder-o', 'br'],
		 'folder_open':     ['folder-open', 'br', False],
		 'folder_close':    ['folder', 'br'],
		 'shopping_cart':   ['shopping-cart', 'br', False],
		 'comment':         ['comment', 'br'],
		 'calendar':        ['calendar', 'br', False],
		 'picture':         ['picture-o', 'br'],
		 'inbox':           ['inbox', 'br'],
		 'filter':          ['filter', 'br'],
		 'facetime_video':  ['video-camera', 'br'],
		 'save':            ['floppy-o', 'br'],
		 '_388':            ['graduation-cap', 'br', False],
		 'question_sign':   ['question-circle', 'br'],
		 'cloud':           ['cloud', 'br'],
		 'heart':           ['heart', 'br', False],
		 'heart_empty':     ['heart-o', 'br'],
		 'group':           ['group', 'br'],
		 'globe':			['globe', 'br', False],
		 '_593':            ['map-o', 'br'],
		 '_594':            ['map', 'br', False],
		 'cog':             ['cog', 'br'],
		 '_591':            ['map-pin', 'br'],
		 '_616':            ['shopping-basket', 'br'],
		 '_615':            ['shopping-bag', 'br'],
		 '_618':            ['bluetooth', 'br'],
		 '_619':            ['bluetooth-b', 'br'],
		 'tasks':           ['tasks', 'br'],
		 'credit_card':     ['credit-card', 'br'],
		 'headphones':      ['headphones', 'br'],
		 'phone':           ['phone', 'br'],
		 'archive':         ['archive', 'br']
		 }

operators = {'plus': 'plus',
			 'minus': 'minus',
			 'ok': 'check',
			 'remove': 'remove',
			 'cog': 'cog',
			 'warning_sign': 'exclamation-triangle',
			 'remove_sign': 'times-circle',
			 'ok_sign': 'check-circle',
			 'question': 'question',
			 '_279': 'info',
			 'ban_circle': 'ban',
			 'star': 'star',
			 'refresh': 'refresh',
			 'search': 'search',
			 'pencil': 'pencil',
			 'trash': 'trash',
			 'envelope_alt': 'envelope',
			 'time': 'clock-o',
			 'tag': 'tag',
			 'arrow_right': 'arrow-right',
			 'file_text': 'file-text',
			 'music': 'music'}

defined_css_rules = []

# Remove previous data
from subprocess import call
call(["rm", "-rf", "./dist"])
call(["mkdir", "./dist"])
call(["mkdir", "./dist/css"])
call(["mkdir", "./dist/fonts"])
call(["cp", "./fontawesome/css/font-awesome.css", "./dist/css/font-awesome.css"])

# Load font
font = fontforge.open('fontawesome/fonts/fontawesome-webfont.ttf')

# and now the automated process

a = psMat.scale(0.6)
a2 = psMat.scale(0.6)
cur_unicode = start_char

icon_list = []

# Detects if the next unicode character is a blacklisted one
def next_unicode(cur_unicode):
	new_unicode = cur_unicode + 1
	while new_unicode in range(0xfe00, 0xfe10) or new_unicode == 0xfeff or new_unicode in range(0xf000, 0xf2ff):
		new_unicode = new_unicode + 1
	return new_unicode


if output_css:
	css = open('./dist/css/font-awesome-appendix.css', 'w')

if output_list:
	with open('./README.tpl.md', 'r') as content_file:
		readme_template = content_file.read()

if output_html:
	html = open('demo.html', 'w')
	html.write('<!DOCTYPE html>\n')
	html.write('<html>\n')
	html.write('<head>\n')
	html.write('<title>fontawesome actions test</title>\n')
	html.write('<meta charset="utf-8">\n')
	if compress_css:
		html.write('<link rel="stylesheet" type="text/css" href="dist/css/font-awesome.min.css">\n')
	else:
		html.write('<link rel="stylesheet" type="text/css" href="dist/css/font-awesome.css">\n')
	html.write('</head>\n')
	html.write('<body>\n')

if generate_combined_icons:
	html.write('<h1>Combined Icons</h1>\n')
	html.write('<table>\n')
	html.write('<thead>\n')
	html.write('<tr>\n')
	html.write('<td></td>\n')
	for operator, css_name in operators.iteritems():
		html.write('<td><i class="fa fa-'+css_name+' fa-3x"></i></td>\n')
	html.write('</tr>\n')
	html.write('</thead>\n')
	html.write('<tbody>\n')

	for icon, options in icons.iteritems():
		print(options[0])
		glyph = font[icon]
		position = options[1]
		if output_html:
			html.write('<tr>\n')
			html.write('<td><i class="fa fa-'+options[0]+' fa-3x"></i></td>\n')

		for operator, css_operator in operators.iteritems():
			print(' & ' + operator)
			circle = font[operator]
			font.selection.select(operator)
			font.copy()
			font.selection.select(("unicode", None), cur_unicode)
			font.paste()
			if position == 'br':
				b = psMat.translate(glyph.width - circle.width * 0.4 * horizontal_shifting,0)
				b2 = psMat.translate(glyph.width - circle.width * 0.375 * horizontal_shifting,0)
			elif position == 'tr':
				b = psMat.translate(glyph.width - circle.width * 0.4 * horizontal_shifting,circle.vwidth * 0.3)
				b2 = psMat.translate(glyph.width - circle.width * 0.375 * horizontal_shifting,circle.vwidth * 0.3)

			font[cur_unicode].changeWeight(outline_border_weight)
			font[cur_unicode].transform(a)
			font[cur_unicode].transform(b)
			font[cur_unicode].removeOverlap()
			font[cur_unicode].exclude(glyph.layers[1])



			font.selection.select(operator)
			font.copy()
			font.selection.select(("unicode", None), workbench_char)
			font.paste()
			font[workbench_char].transform(a2)
			font[workbench_char].transform(b2)
			font.copy()
			font.selection.select(("unicode", None), cur_unicode)
			font.pasteInto()
			font.correctDirection()

			icon_list.append(options[0] + '-' + css_operator)
			css_name = 'fa-' + options[0] + '-' + css_operator
			defined_css_rules.append(css_name)

			if output_css:
				css.write('.' + css_name + ':before { content: "\\'+(hex(cur_unicode)[2:])+'"; }\n')

			if output_html:
				html.write('<td><i class="fa '+css_name+' fa-2x"></i></td>\n')

			cur_unicode = next_unicode(cur_unicode)
		if output_html:
			html.write('</tr>\n')
	if output_html:
		html.write('</tbody>\n')
		html.write('</table>\n')

if generate_splitted_icons:
	if output_css:
		css.write('.fa-action-stack { position: relative; display: inline-block; width: 4em; height: 2em; line-height: 2em; vertical-align: middle;}\n')

	import random
	colors = ['#001f3f','#0074D9','#7FDBFF','#39CCCC','#3D9970','#2ECC40','#01FF70','#FFDC00','#FF851B','#FF4136','#85144b','#F012BE','#B10DC9']
	html.write('<h1>Splitted Icons</h1>\n')
	html.write('<table>\n')
	html.write('<thead>\n')
	html.write('<tr>\n')
	html.write('<td></td>\n')
	for operator, css_name in operators.iteritems():
		html.write('<td><i class="fa fa-'+css_name+' fa-3x"></i></td>\n')
	html.write('</tr>\n')
	html.write('</thead>\n')
	html.write('<tbody>\n')

	for icon, options in icons.iteritems():
		print(options[0])
		glyph = font[icon]
		position = options[1]
		if output_html:
			html.write('<tr>\n')
			html.write('<td><i class="fa fa-'+options[0]+' fa-3x"></i></td>\n')

		for operator, css_operator in operators.iteritems():
			circle = font[operator]
			font.selection.select(operator)
			font.copy()
			font.selection.select(("unicode", None), cur_unicode)
			font.paste()

			if position == 'br':
				b = psMat.translate(glyph.width - circle.width * 0.4 * horizontal_shifting,0)
				b2 = psMat.translate(glyph.width - circle.width * 0.375 * horizontal_shifting,0)
			elif position == 'tr':
				b = psMat.translate(glyph.width - circle.width * 0.4 * horizontal_shifting,circle.vwidth * 0.3)
				b2 = psMat.translate(glyph.width - circle.width * 0.375 * horizontal_shifting,circle.vwidth * 0.3)

			font[cur_unicode].changeWeight(outline_border_weight)
			font[cur_unicode].transform(a)
			font[cur_unicode].transform(b)
			font[cur_unicode].removeOverlap()
			font[cur_unicode].exclude(glyph.layers[1])
			font.correctDirection()

			font.selection.select(operator)
			font.copy()
			font.selection.select(("unicode", None), workbench_char)
			font.paste()
			font[workbench_char].transform(a2)
			font[workbench_char].transform(b2)
			font.copy()
			first_unicode = cur_unicode
			cur_unicode = next_unicode(cur_unicode)
			second_unicode = cur_unicode
			font.selection.select(("unicode", None), cur_unicode)
			font.paste()
			font.correctDirection()

			icon_list.append(options[0] + '-' + css_operator + '-alpha')
			icon_list.append(options[0] + '-' + css_operator + '-beta')
			css_name = 'fa-' + options[0] + '-' + css_operator

			if output_css:
				css.write('.' + css_name + '-alpha:before { content: "\\'+(hex(first_unicode)[2:])+'"; }\n')
				css.write('.' + css_name + '-beta:before { content: "\\'+(hex(second_unicode)[2:])+'"; }\n')

			if output_html:
				html.write('<td><span class="fa-stack"><i class="fa '+css_name+'-beta fa-2x fa-stack-1x" style="color: '+random.choice(colors)+';"></i><i class="fa '+css_name+'-alpha fa-2x fa-stack-1x"></i></span></td>\n')

			cur_unicode = next_unicode(cur_unicode)
		if output_html:
			html.write('</tr>\n')
	if output_html:
		html.write('</tbody>\n')
		html.write('</table>\n')

if generate_slashed_icons:
	html.write('<h1>Slashed Icons</h1>\n')
	html.write('<table>\n')
	html.write('<tbody>\n')
	html.write('<tr>\n')
	html.write('<td><i class="fa fa-bell fa-2x"></i></td>\n')
	html.write('<td><i class="fa fa-bell-slash fa-2x"></i></td>\n')
	html.write('</tr>\n')

	for icon, options in icons.iteritems():
		print(options[0])
		glyph = font[icon]
		position = options[1]
		if output_html:
			html.write('<tr>\n')
			html.write('<td><i class="fa fa-'+options[0]+' fa-2x"></i></td>\n')

		circle = font['minus']
		font.selection.select('minus')
		font.copy()

		font.selection.select(("unicode", None), workbench_char)
		font.paste()

		x = (font[icon].boundingBox()[2] - font[icon].boundingBox()[0]) / 2.0
		y = (font[icon].boundingBox()[3] - font[icon].boundingBox()[1]) / 2.0
		s = psMat.scale(1.7,0.5)
		font[workbench_char].transform(s)
		r = psMat.rotate(3.1415926535/4.0)
		font[workbench_char].transform(r)
		t = psMat.translate(x-500,y-1400)
		font[workbench_char].transform(t)

		font.selection.select(("unicode", None), workbench_char)
		font.copy()

		font.selection.select(("unicode", None), cur_unicode)
		font.paste()

		t = psMat.translate(-160,120)
		font[workbench_char].transform(t)

		font.selection.select(("unicode", None), workbench_char)
		font.copy()

		font.selection.select(("unicode", None), cur_unicode)
		font.pasteInto()

		font[cur_unicode].exclude(font[icon].layers[1])

		font.selection.select(("unicode", None), cur_unicode)
		font.pasteInto()

		font.removeOverlap()

		font.correctDirection()

		font[cur_unicode].width = glyph.width

		icon_list.append(options[0] + '-slash')
		css_name = 'fa-' + options[0] + '-slash'

		if output_css:
			defined_css_rules.append(css_name)
			css.write('.' + css_name + ':before { content: "\\'+(hex(cur_unicode)[2:])+'"; }\n')

		if output_html:
			html.write('<td><i class="fa '+css_name+' fa-2x"></i></td>\n')

		cur_unicode = next_unicode(cur_unicode)
		if output_html:
			html.write('</tr>\n')
	if output_html:
		html.write('</tbody>\n')
		html.write('</table>\n')


if generate_stroked_icons:
	html.write('<h1>Stroked Icons</h1>\n')
	html.write('<table>\n')
	html.write('<tbody>\n')

	for icon, options in icons.iteritems():
		if options[0].endswith('-o'):
			continue
		if len(options) >= 3 and not options[2]:
			continue
		print(options[0])
		glyph = font[icon]
		position = options[1]
		if output_html:
			html.write('<tr>\n')
			html.write('<td><i class="fa fa-'+options[0]+' fa-2x"></i></td>\n')

		font.selection.select(glyph)
		font.copy()

		font.selection.select(("unicode", None), cur_unicode)
		font.paste()

		font[cur_unicode].stroke('circular', 100, 'round', 'round', ('cleanup'))

		#font.simplify(10)
		font.removeOverlap()

		font.correctDirection()

		icon_list.append(options[0] + '-o')
		css_name = 'fa-' + options[0] + '-o'

		if output_css:
			defined_css_rules.append(css_name)
			css.write('.' + css_name + ':before { content: "\\'+(hex(cur_unicode)[2:])+'"; }\n')

		if output_html:
			html.write('<td><i class="fa '+css_name+' fa-2x"></i></td>\n')

		cur_unicode = next_unicode(cur_unicode)
		if output_html:
			html.write('</tr>\n')
	if output_html:
		html.write('</tbody>\n')
		html.write('</table>\n')



if output_css:
	css.close()

	# cleanup pre existant css rules that are conflicting with newly generated ones
	print 'cleanup ...'
	css = open('./dist/css/font-awesome.css', 'r')
	text = css.read()
	css.close()

	for rule in defined_css_rules:
		print rule
		text = re.sub(r'\.'+rule+':before {\n(.*)\n}', '', text)


	css = open('./dist/css/font-awesome-appendix.css', 'r')
	appendix_text = css.read()
	css.close()

	css = open('./dist/css/font-awesome.css', 'w')
	css.write(text)
	css.write(appendix_text)
	css.close()

	call(['rm', './dist/css/font-awesome-appendix.css'])

	print 'done'

	if compress_css:
		css = open('./dist/css/font-awesome.css', 'r')
		text = css.read()
		css.close()

		import css_compress

		css = open('./dist/css/font-awesome.min.css', 'w')
		css.write(css_compress.compress(text))
		css.close()


if output_html:
	html.write('</body>')
	html.write('</html>')
	html.close()

if output_list:
	print('generating README.md')
	list = open('./README.md', 'w')

	with open('./fontawesome/README.md', 'r') as content_file:
		fa_readme = content_file.read()

	m = re.search('# \[Font Awesome v([0-9\.]+)\]\((.*)\)',fa_readme)
	readme_template = readme_template.replace('[[VERSION]]', m.group(1))

	m = re.search('Font Awesome is a full suite of ([0-9]+) pictographic icons for easy scalable vector graphics on websites,', fa_readme)
	orig_count = int(m.group(1))
	readme_template = readme_template.replace('[[ORIG-COUNT]]', m.group(1))

	readme_template = readme_template.replace('[[NEW-COUNT]]', str(len(icon_list) + orig_count))

	list.write(readme_template)

	for icon in icon_list:
		list.write('* ' + icon + '\n')

	list.close()

print('[FontForge] generating dist/fonts/fontawesome-webfont.woff')
font.generate('dist/fonts/fontawesome-webfont.woff')
print('[FontForge] generating dist/fonts/fontawesome-webfont.ttf')
font.generate('dist/fonts/fontawesome-webfont.ttf')
print('[FontForge] generating dist/fonts/fontawesome-webfont.svg')
font.generate('dist/fonts/fontawesome-webfont.svg')
print('[FontForge] generating dist/fonts/FontAwesome.otf')
font.generate('dist/fonts/FontAwesome.otf')
print('[ttf2eot] generating dist/fonts/fontawesome-webfont.eot')
call("./ttf2eot < dist/fonts/fontawesome-webfont.ttf > dist/fonts/fontawesome-webfont.eot", shell=True)
print('[woff2_compress] generating dist/fonts/fontawesome-webfont.woff2')
call("./woff2_compress dist/fonts/fontawesome-webfont.ttf", shell=True)

print('DONE! generated ' + str(len(icon_list)) + ' glyphs')
