file1 = open('src/gui.py', 'r')
lines = file1.readlines()

TO_FIND = '        self.pdfTreeWidget = QtWidgets.QTreeWidget(self.centralwidget)\n'
TO_PUT  = '        self.pdfTreeWidget = tree.TreeWidget(self.centralwidget)\n'

i = 1
for line in lines:
    if line.strip().__eq__(TO_FIND.strip()):
        lines[i-1] = TO_PUT
        break;
    i = i + 1

lines[11] = 'import tree as tree\n'
file1.close()

file2 = open('src/gui.py', 'w')
file2.writelines(lines)
file2.close()
