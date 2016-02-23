import glob
import fnmatch

def parse_output(list_files):
    list_string = ','.join(list_files)
    if len(list_files) > 0:
        print "Files with problem: %s | FILES_WITH_PROBLEM=%s" % (list_string, len(list_files))
        exit(2)
    else:
        print "Perfdata OK | FILES_WITH_PROBLEM=0"
        exit(0)


l = []
path = "/usr/local/nagios/share/perfdata/*/*"
listing = glob.iglob(path)
aux_list = fnmatch.filter(listing, "*.xml")
for xml in aux_list:
    with open(xml) as f:
        content = f.read()
        if '<RC>1</RC>' in content:
           l.append('/'.join(xml.split('/')[-2::]))

parse_output(l)