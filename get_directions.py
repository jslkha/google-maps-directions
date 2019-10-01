import sys
import webbrowser

base_url = "https://www.google.co.uk/maps/dir/"
destinations = sys.argv[1:]

if len(sys.argv) > 1 and len(sys.argv) < 11:
    final_url = base_url
    
    for destination in destinations:
        final_url += str(destination + "/")

    print(final_url)
    
    webbrowser.get('chrome').open_new_tab(final_url)
else:
    print("Error: Number of locations should be greater than 1 and less than 11")


# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array