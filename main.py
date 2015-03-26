import fontforge
import psMat

# settings
output_html = True
output_css = True
workbench_char = 0xf2ff
start_char = 0xf300
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

operators = {'plus': 'plus', 'minus': 'minus', 'ok': 'check', 'remove': 'remove', 'cog': 'cog'}

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
	print icon
	bookmark = font[icon]
	position = options[1]
	if output_html:
		html.write('<tr>\n')
		html.write('<td><i class="fa fa-'+options[0]+' fa-3x"></i></td>\n')

	for operator, _ in operators.iteritems():
		circle = font[operator]
		font.selection.select(operator)
		font.copy()
		font.selection.select(("unicode", None), cur_unicode)
		font.paste()
		if position == 'br':
			b = psMat.translate(bookmark.width - circle.width * 0.4 * 0.7,0)
			b2 = psMat.translate(bookmark.width - circle.width * 0.375 * 0.7,0)
		elif position == 'tr':
			b = psMat.translate(bookmark.width - circle.width * 0.4 * 0.7,circle.vwidth * 0.3)
			b2 = psMat.translate(bookmark.width - circle.width * 0.375 * 0.7,circle.vwidth * 0.3)

		font[cur_unicode].changeWeight(320)
		font[cur_unicode].transform(a)
		font[cur_unicode].transform(b)
		font[cur_unicode].exclude(bookmark.layers[1])

		font.selection.select(operator)
		font.copy()
		font.selection.select(("unicode", None), workbench_char)
		font.paste()
		font[workbench_char].transform(a2)
		font[workbench_char].transform(b2)
		font.copy()
		font.selection.select(("unicode", None), cur_unicode)
		font.pasteInto()

		css_name = 'fa-' + options[0] + '-' + operator
		
		if output_css:
			css.write('.' + css_name + ':before { content: "\\'+(hex(cur_unicode)[2:])+'"; }\n')

		if output_html:
			html.write('<td><i class="fa '+css_name+' fa-3x"></i></td>\n')

		cur_unicode = cur_unicode + 1
	if output_html:
		html.write('</tr>\n')
	
if output_css:
	css.close()

if output_html:
	html.write('</tbody>\n')
	html.write('</table>\n')
	html.write('</body>')
	html.write('</html>')
	html.close()

font.generate('dist/fonts/fontawesome-webfont.woff')
font.generate('dist/fonts/fontawesome-webfont.ttf')
font.generate('dist/fonts/fontawesome-webfont.svg')
font.generate('dist/fonts/FontAwesome.otf')
call("./ttf2eot < dist/fonts/fontawesome-webfont.ttf > dist/fonts/fontawesome-webfont.eot", shell=True)
call("./woff2_compress dist/fonts/fontawesome-webfont.ttf", shell=True)
