import codecs
from winsys import fs

base = "c:/temp"
with codecs.open ("C:\\Users\\your_username\\Documents\\permissions.log", "wb", encoding="utf8") as log:
  for f in fs.flat (base):
      log.write ("\n" + f.filepath.relative_to (base) + "\n")
      for ace in f.security ().dacl:
        access_flags = fs.FILE_ACCESS.names_from_value (ace.access)
        log.write (u"  %s => %s\n" % (ace.trustee, ", ".join (access_flags)))
