# Створення фрактала “дерево Піфагора” за допомогою рекурсії
import turtle

def draw_branch(level, max_level, length, angle):
    if level > max_level:
        return

    turtle.forward(length)
    turtle.right(angle)
    draw_branch(level + 1, max_level, length * 0.75, angle)
    turtle.left(angle * 2)
    draw_branch(level + 1, max_level, length * 0.75, angle)
    turtle.right(angle)
    turtle.backward(length)

def main():
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color("brown")

    try:
        max_level = int(input("Вкажіть рівень рекурсії (наприклад, 5-10): "))
        if max_level < 1:
            raise ValueError("Рівень має бути > 0")
    except ValueError as e:
        print(f"Помилка: {e}")
        return

    draw_branch(1, max_level, 100, 50) # Рівні кута та розгалудження підібрані шляхом кількох тестів, ці є оптимальними та наближеними до прикладу у завданні
    turtle.done()

main()