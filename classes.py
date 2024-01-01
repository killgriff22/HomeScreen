from modules import *
class Screen:
    def __init__(self,size:tuple,pos:tuple) -> None:
        self.size = size
        self.pos = pos
        self.content=[[" "]*self.size[0] for _ in range(self.size[1])]
    def draw(self) -> None:
        for i,line in enumerate(self.content):
            if len(line)-1 > self.size[0]:
                self.clear()
                print_at(self.pos[0]+1,self.pos[1]+1,f"line {i} too long!\n{len(line)}\ncropping line for next frame!")
                self.content[i] = self.content[i][:-(len(line)-self.size[0])]
                return
            #print(line)
            compiled = "".join(line)
            print_at(self.pos[0]+1,self.pos[1]+i+1,compiled)
    def clear(self) -> None:
        lines=[]
        for i in range(self.size[1]):
            lines.append(" "*self.size[0])
        for i,line in enumerate(lines):
            print_at(self.pos[0]+1,self.pos[1]+i+1,line)
    def fill(self,char:str) -> None:
        for x in range(0,self.size[0]):
            for y in range(0,self.size[1]):
                self.content[y][x] = char
        return
class Process:
    def __init__(self,screen:Screen,path:str or os.PathLike, args:list[str]=[]):
        self.screen = screen
        self.output=str()
        self.Process = subprocess.Popen([path]+args,stdout=self.output)
    def draw(self):
        for x,char in self.output:
            y=x//self.screen.size[0]
            self.screen.content[y][x] = char