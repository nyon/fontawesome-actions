import fontforge
import psMat

# settings
output_html = True
output_css = True
generate_combined_icons = True
generate_splitted_icons = True
workbench_char = 0xf2ff
start_char = 0xf300
outline_border_weight = 320
horizontal_shifting = 0.7
icons = {'bookmark':        ['bookmark', 'tr'],
		 'user':            ['user', 'br'],
		 '_407':            ['cube', 'br'],
		 'camera':          ['camera', 'br'],
		 'tag':             ['tag', 'br'],
		 'tags':            ['tags', 'br'],
		 'uniF1C0':         ['database', 'br'],
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
		 'file_text':       ['file-text','br'],
		 'file_text_alt':   ['file-text-o','br'],
		 'envelope_alt':    ['envelope','br'],
		 'link':            ['link','br'],
		 'folder_open_alt': ['folder-open-o', 'br'],
		 'folder_close_alt':['folder-o', 'br'],
		 'folder_open':     ['folder-open', 'br'],
		 'folder_close':    ['folder', 'br'],
		 'shopping_cart':   ['shopping-cart', 'br'],
		 'comment':         ['comment', 'br'],
		 'calendar':        ['calendar', 'br'],
		 'picture':         ['picture-o', 'br'],
		 'inbox':           ['inbox', 'br']
		 }

operators = {'plus': 'plus', 'minus': 'minus', 'ok': 'check', 'remove': 'remove', 'cog': 'cog', 'warning_sign': 'exclamation-triangle', 'remove_sign': 'times-circle', 'ok_sign': 'check-circle'}

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

if output_css:
	css = open('./dist/css/font-awesome.css', 'a+')

if output_html:
	html = open('demo.html', 'w')
	html.write('<!DOCTYPE html>\n')
	html.write('<html>\n')
	html.write('<head>\n')
	html.write('<title>fontawesome actions test</title>\n')
	html.write('<meta charset="utf-8">\n')
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
#			font[cur_unicode].exclude(glyph.layers[1])



			font.selection.select(operator)
			font.copy()
			font.selection.select(("unicode", None), workbench_char)
			font.paste()
			font[workbench_char].transform(a2)
			font[workbench_char].transform(b2)
			font.copy()
			font.selection.select(("unicode", None), cur_unicode)
			font.pasteInto()

			css_name = 'fa-' + options[0] + '-' + css_operator

			if output_css:
				css.write('.' + css_name + ':before { content: "\\'+(hex(cur_unicode)[2:])+'"; }\n')

			if output_html:
				html.write('<td><i class="fa '+css_name+' fa-2x"></i></td>\n')

			cur_unicode = cur_unicode + 1
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
			font[cur_unicode].exclude(glyph.layers[1])

			font.selection.select(operator)
			font.copy()
			font.selection.select(("unicode", None), workbench_char)
			font.paste()
			font[workbench_char].transform(a2)
			font[workbench_char].transform(b2)
			font.copy()
			font.selection.select(("unicode", None), cur_unicode+1)
			font.paste()

			css_name = 'fa-' + options[0] + '-' + css_operator

			if output_css:
				css.write('.' + css_name + '-alpha:before { content: "\\'+(hex(cur_unicode)[2:])+'"; }\n')
				css.write('.' + css_name + '-beta:before { content: "\\'+(hex(cur_unicode+1)[2:])+'"; }\n')

			if output_html:
				html.write('<td><span class="fa-stack"><i class="fa '+css_name+'-beta fa-2x fa-stack-1x" style="color: '+random.choice(colors)+';"></i><i class="fa '+css_name+'-alpha fa-2x fa-stack-1x"></i></span></td>\n')

			cur_unicode = cur_unicode + 2
		if output_html:
			html.write('</tr>\n')
	if output_html:
		html.write('</tbody>\n')
		html.write('</table>\n')



if output_css:
	css.close()

if output_html:
	html.write('</body>')
	html.write('</html>')
	html.close()

font.generate('dist/fonts/fontawesome-webfont.woff')
font.generate('dist/fonts/fontawesome-webfont.ttf')
font.generate('dist/fonts/fontawesome-webfont.svg')
font.generate('dist/fonts/FontAwesome.otf')
call("./ttf2eot < dist/fonts/fontawesome-webfont.ttf > dist/fonts/fontawesome-webfont.eot", shell=True)
call("./woff2_compress dist/fonts/fontawesome-webfont.ttf", shell=True)

print('generated ' + str(cur_unicode - start_char) + ' glyphs')