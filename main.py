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
		 'uniF1C1':         ['pdf', 'br'],
		 '_422':            ['word', 'br'],
		 '_423':            ['xls', 'br'],
		 '_424':            ['powerpoint', 'br'],
		 '_425':            ['image', 'br'],
		 '_426':            ['zip', 'br'],
		 '_427':            ['audio', 'br'],
		 '_428':            ['video', 'br'],
		 '_429':            ['code', 'br'],
		 'file':            ['file', 'br'],
		 'file_text':       ['file-text','br'],
		 'file_text_alt':   ['file-text-alt','br'],
		 'envelope_alt':    ['envelope-alt','br'],
		 'link':            ['link','br'],
		 'folder_open_alt': ['folder-open-alt', 'br'],
		 'folder_close_alt':['folder-close-alt', 'br'],
		 'folder_open':     ['folder-open', 'br'],
		 'folder_close':    ['folder-close', 'br'],
		 'shopping_cart':   ['shopping-cart', 'br'],
		 'comment':         ['comment', 'br'],
		 'calendar':        ['calender', 'br'],
		 'picture':         ['picture', 'br'],
		 'inbox':           ['inbox', 'br']
		 }

operators = ['plus', 'minus', 'ok', 'remove', 'cog']

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


for icon, options in icons.iteritems():
	print icon
	bookmark = font[icon]
	position = options[1]

	for operator in operators:
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
			html.write('<i class="fa '+css_name+'"></i> <i class="fa '+css_name+' fa-2x"></i> <i class="fa '+css_name+' fa-3x"></i><br>\n')

		cur_unicode = cur_unicode + 1

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
