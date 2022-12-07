from common import read_lines


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.files = []
        self.folders: list["Directory"] = []
        self.parent = parent
    
    def get_folder(self, name):
        if name == "..":
            return self.parent

        for folder in self.folders:
            if folder.name == name:
                return folder
        
        folder = Directory(name, self)
        self.folders.append(folder)
        return folder

    def add_file(self, name, size: int):
        self.files.append((size, name))

    def total_size(self):
        size = 0
        for subfolder in self.folders:
            size += subfolder.total_size()
        for filesize, _ in self.files:
            size += filesize

        return size


class Context:
    def __init__(self):
        self.root = Directory(name="/", parent=None)
        self.current = self.root

    def cd(self, path):
        if path=="/":
            self.current = self.root
        else:
            print(f"Entering {path}")
            self.current = self.current.get_folder(path)

    def print_structure(self):
        def visit(dir, indent):
            print(" "*indent + dir.name + f" (dir) {dir.total_size()}")
            for subdir in dir.folders:
                visit(subdir, indent+2)
            for size, filename in dir.files:
                print(" "*(indent+2) + filename + f" ({size})")

        visit(self.root, 0)

    def find_with_min_size(self, min_req_size):
        def visit(dir: Directory, result: list[Directory]):
            if dir.total_size() >= min_req_size:
                result.append(dir)
            for subdir in dir.folders:
                visit(subdir, result)

            return result

        return visit(self.root, [])



lines = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split("\n")

lines = read_lines("input07.txt")

context = Context()
for line in lines:
    if line.startswith("$"):
        cmd_line = line.split(" ")
        cmd = cmd_line[1]
        arg = cmd_line[2] if len(cmd_line)>2 else None
        if cmd == "cd":
            context.cd(arg)
    else: # Assume we are seeing contents of a ls command
        output = line.split(" ")
        if output[0] == "dir":
            pass # Do nothing as we assume we will visit it
        else:
            context.current.add_file(output[1], int(output[0]))

def visit(dir: Directory, sum, indent = 0):
    size = dir.total_size()
    if size <= 100000:
        sum += size
    
    for subdir in dir.folders:
        sum = visit(subdir, sum, indent=indent+2)
    
    return sum

result = visit(context.root, 0)
print(result)

total_size = 70000000
required_space = 30000000
free_space = total_size - context.root.total_size()
print(f"Free space: {free_space}")
minimum_required_space = required_space - free_space
print(f"Required space to free up: {minimum_required_space}")

possible_dirs = context.find_with_min_size(minimum_required_space)

print(min([x.total_size() for x in possible_dirs]))