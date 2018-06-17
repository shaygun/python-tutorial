#Escape Sequence
#\\ Backslash (\)
#\' Single-quote (') \" Double-quote (")
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N{name} Character named name in the Unicode database (Unicode only)
#\r ASCII carriage return (CR) - it replace the charecter with new items
#\t ASCII horizontal tab (TAB)

# Example 1
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

==>   I'm tabbed in.
==>I'm split
==>on a line.
==>I'm \ a \ cat.
==>I'll do a list:
==>     * Cat food
==>     * Fishies
==>     * Catnip
==>     * Grass

# Example 2
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
==> loading sign
