##
# Main function of the Python program.
#
##

from aloca import aloca

def main():
    print("<h3>aloca</h3>")
    prefs = {10885:[1,5],40000:[5],10000:[1,2]}
    print("in:",prefs)
    print("out:",aloca(prefs))

if __name__ == '__main__':
    main()
