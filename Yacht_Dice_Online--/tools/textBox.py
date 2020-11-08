import os
import pygame

# 텍스트 상자
class textBox:
    def __init__(self, font, color, rect, text = ""):
        if not os.path.isfile(font):
            font = pygame.font.match_font(font)
            
        self.font = pygame.font.Font(font, rect[3] - 8)
        self.COLOR = color
        self.RECT = rect
        self.text = text
        self.cursor = 0
        self.startpos = 0
        self.active = False
        self.mouseheld = False
        self.shiftheld = False
        self.selected = None
        self.clock = pygame.time.Clock()
        self.time = 0
        self.visible = True
        self.SWITCHTIME = 600
        self.surf = pygame.Surface(rect[2:])
    
    # 텍스트 표시
    def renderText(self, indices=None):
        if indices is None:
            indices = [0, len(self.text)]
            
        return self.font.render(
            self.text[indices[0]:indices[1]], True, self.COLOR)
        
    # 텍스트 입력
    def insert(self, index, text):
        self.text = self.text[:index] + text + self.text[index:]
    
    # 텍스트 삭제
    def remove(self, indices):
        if isinstance(indices, int):
            indices = [indices, indices + 1]
        self.text = self.text[:indices[0]] + self.text[indices[1]:]
    
    # 텍스트 길이
    def getLen(self, indices=None):
        return self.renderText(indices).get_width()
           
    # 이벤트 핸들링
    def push(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouseheld = True
            x, y = event.pos
            if (self.RECT[0] < x < (self.RECT[0] + self.RECT[2]) and
                self.RECT[1] < y < (self.RECT[1] + self.RECT[3])):
                self.active = True
            else:
                self.active = False               
            
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouseheld = False
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                self.shiftheld = False
            
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key in [pygame.K_TAB, pygame.K_ESCAPE, pygame.K_KP_ENTER]:
                pass
            
            elif event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                self.shiftheld = True
            
            elif event.key == pygame.K_BACKSPACE:
                if self.selected is None:
                    if self.cursor > 0:
                        self.cursor -= 1
                        self.remove(self.cursor)
                else:
                    self.cursor = self.selected[0]
                    self.remove(self.selected)
                    self.selected = None
                    
            elif event.key == pygame.K_DELETE:
                if self.selected is None:
                    if self.cursor < len(self.text):
                        self.remove(self.cursor)
                else:
                    self.cursor = self.selected[0]
                    self.remove(self.selected)
                    self.selected = None
                        
            elif event.key == pygame.K_RIGHT:
                if self.cursor < len(self.text):
                    self.cursor += 1
                    if self.shiftheld:
                        if self.selected is None:
                            self.selected = [self.cursor - 1, self.cursor]
                        elif self.cursor == self.selected[1] + 1:
                            self.selected[1] += 1
                        
                        if self.selected[0] == self.selected[1]:
                            self.selected = None
                            
                    else:
                        self.selected = None

            elif event.key == pygame.K_LEFT:
                if self.cursor > 0:
                    self.cursor -= 1
                    if self.shiftheld:
                        if self.selected is None:
                            self.selected = [self.cursor, self.cursor + 1]
                        elif self.cursor == self.selected[0] - 1:
                            self.selected[0] -= 1
                            
                        if self.selected[0] == self.selected[1]:
                            self.selected = None
                            
                    else:
                        self.selected = None
                        
            elif event.key == pygame.K_END:
                if self.cursor < len(self.text):
                    if self.shiftheld:
                        if self.selected is None:
                            self.selected = [self.cursor, len(self.rendered)]
                        else:
                            self.selected[1] = len(self.rendered)
                    else:
                        self.selected = None
                    self.cursor = len(self.text)

            elif event.key == pygame.K_HOME:
                if self.cursor > 0:
                    if self.shiftheld:
                        if self.selected is None:
                            self.selected = [0, self.cursor]
                        else:
                            self.selected[0] = 0
                    else:
                        self.selected = None
                    self.cursor = 0
                
            elif event.key == pygame.K_RETURN:
                self.active = False
                
            elif len(event.unicode) == 1:
                if self.selected is None:
                    self.insert(self.cursor, event.unicode)
                    self.cursor += 1
                else:
                    self.remove(self.selected)
                    self.cursor = self.selected[0]
                    self.selected = None
                    self.insert(self.cursor, event.unicode)
                    self.cursor += 1

    # 텍스트 사각형 그리기       
    def draw(self, win):
        self.time += self.clock.get_time()
        if self.time >= self.SWITCHTIME:
            self.time %= self.SWITCHTIME
            self.visible = not self.visible
        
        self.surf.fill((0, 0, 0))
        pygame.draw.rect(self.surf, (255, 255, 255),
                         (3, 3, self.RECT[2] - 6, self.RECT[3] - 6))
        
        cursorpos = self.getLen([0, self.cursor])
        
        rendered = pygame.Surface((self.getLen() + 2, self.RECT[3] - 8))
        rendered.fill((255, 255, 255))
           
        if self.selected is not None:
            selrect = (self.getLen([0, self.selected[0]]), 2,
                       self.getLen(self.selected), self.RECT[3] - 12)
            pygame.draw.rect(rendered, (128, 220, 255), selrect)
            
        rendered.blit(self.renderText(), (0, 0))
        
        if self.active:
            pygame.draw.rect(self.surf, (0, 0, 255),
                         (2, 2, self.RECT[2] - 5, self.RECT[3] - 5), 2)
            
            if self.visible:
                pygame.draw.line(rendered, (0, 0, 0), (cursorpos, 2),
                                 (cursorpos, self.RECT[3] - 12), 2)
        
        if rendered.get_width() > self.RECT[2] - 8:
            if cursorpos < self.startpos + 2:
                self.startpos = cursorpos - 2
            elif cursorpos > self.startpos + self.RECT[2] - 6:
                self.startpos = cursorpos - self.RECT[2] + 6
            else:
                self.surf.blit(rendered, (4 - self.startpos, 4))
        else:
            self.surf.blit(rendered, (4, 4))
            
        win.blit(self.surf, self.RECT[:2])
        self.clock.tick()                        
