from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from random import randint
from kivy.core.window import Window

# Cấu hình cửa sổ game
Window.size = (400, 400)

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cell_size = 20
        self.snake = [(5, 5)]
        self.food = (randint(0, 19), randint(0, 19))
        self.direction = (1, 0)  # Di chuyển sang phải
        self.game_over = False

        # Vẽ nền game
        with self.canvas:
            Color(0, 0, 0, 1)
            self.bg = Rectangle(size=Window.size)

        # Vẽ rắn và thức ăn
        self.snake_rects = []
        with self.canvas:
            for segment in self.snake:
                self.snake_rects.append(Rectangle(pos=(segment[0] * self.cell_size, segment[1] * self.cell_size),
                                                  size=(self.cell_size, self.cell_size)))
            Color(1, 0, 0, 1)  # Màu đỏ cho thức ăn
            self.food_rect = Rectangle(pos=(self.food[0] * self.cell_size, self.food[1] * self.cell_size),
                                       size=(self.cell_size, self.cell_size))

        # Hiển thị điểm số
        self.score_label = Label(text="Score: 0", font_size='20sp', pos=(0, 180))
        self.add_widget(self.score_label)

        # Chạy game
        Clock.schedule_interval(self.update, 0.2)
        Window.bind(on_key_down=self.on_key_down)

    def update(self, dt):
        if self.game_over:
            return

        # Di chuyển rắn
        head_x, head_y = self.snake[-1]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Kiểm tra va chạm với tường hoặc chính nó
        if (new_head in self.snake) or not (0 <= new_head[0] < 20 and 0 <= new_head[1] < 20):
            self.game_over = True
            self.score_label.text = "Game Over! Press R to restart"
            return

        self.snake.append(new_head)

        # Kiểm tra ăn thức ăn
        if new_head == self.food:
            self.food = (randint(0, 19), randint(0, 19))
            self.score_label.text = f"Score: {len(self.snake) - 1}"
        else:
            self.snake.pop(0)

        # Cập nhật vị trí rắn và thức ăn
        for i, segment in enumerate(self.snake):
            self.snake_rects[i].pos = (segment[0] * self.cell_size, segment[1] * self.cell_size)

        self.food_rect.pos = (self.food[0] * self.cell_size, self.food[1] * self.cell_size)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if text == 'w' and self.direction != (0, -1):
            self.direction = (0, 1)
        elif text == 's' and self.direction != (0, 1):
            self.direction = (0, -1)
        elif text == 'a' and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif text == 'd' and self.direction != (-1, 0):
            self.direction = (1, 0)
        elif text == 'r':  # Nhấn R để restart
            self.reset_game()

    def reset_game(self):
        self.snake = [(5, 5)]
        self.food = (randint(0, 19), randint(0, 19))
        self.direction = (1, 0)
        self.game_over = False
        self.score_label.text = "Score: 0"

class SnakeApp(App):
    def build(self):
        return SnakeGame()

if __name__ == '__main__':
    SnakeApp().run()
