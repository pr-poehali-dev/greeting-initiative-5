"""
Windows 7 Compatibility Assistant
AI-помощник для запуска приложений Windows 10 на Windows 7

Требования:
- Python 3.6+
- Работает на Windows 7/8/10/11

Создание .exe файла:
pip install pyinstaller
pyinstaller --onefile --windowed --icon=app.ico windows7_compatibility_assistant.py
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import datetime
import os
import sys


class SberAIAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows AI Assistant - Сбер")
        self.root.geometry("1200x700")
        self.root.configure(bg="#0D1117")
        
        # Цветовая схема Сбера
        self.colors = {
            'bg_dark': '#0D1117',
            'bg_card': '#161B22',
            'primary': '#21A038',
            'primary_light': '#30D158',
            'text': '#E6EDF3',
            'text_muted': '#8B949E',
            'border': '#30363D',
            'accent': '#58A55C'
        }
        
        self.setup_styles()
        self.create_widgets()
        self.add_welcome_message()
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Primary.TButton',
                       background=self.colors['primary'],
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       padding=10,
                       font=('Roboto', 10, 'bold'))
        
        style.map('Primary.TButton',
                 background=[('active', self.colors['primary_light'])])
        
        style.configure('Secondary.TButton',
                       background=self.colors['bg_card'],
                       foreground=self.colors['text'],
                       borderwidth=1,
                       bordercolor=self.colors['border'],
                       focuscolor='none',
                       padding=8,
                       font=('Roboto', 9))
        
        style.configure('Card.TFrame',
                       background=self.colors['bg_card'],
                       borderwidth=1,
                       relief='solid')
        
    def create_widgets(self):
        # Главный контейнер
        main_container = tk.Frame(self.root, bg=self.colors['bg_dark'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Хедер
        self.create_header(main_container)
        
        # Контент (чат + боковая панель)
        content_frame = tk.Frame(main_container, bg=self.colors['bg_dark'])
        content_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))
        
        # Левая часть - чат
        self.create_chat_area(content_frame)
        
        # Правая часть - статус и действия
        self.create_sidebar(content_frame)
        
    def create_header(self, parent):
        header = tk.Frame(parent, bg=self.colors['bg_dark'])
        header.pack(fill=tk.X, pady=(0, 10))
        
        # Иконка и название
        icon_frame = tk.Frame(header, bg=self.colors['primary'], width=50, height=50)
        icon_frame.pack(side=tk.LEFT, padx=(0, 15))
        icon_frame.pack_propagate(False)
        
        icon_label = tk.Label(icon_frame, text="🤖", bg=self.colors['primary'],
                             font=('Arial', 24), fg='white')
        icon_label.pack(expand=True)
        
        title_frame = tk.Frame(header, bg=self.colors['bg_dark'])
        title_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        title = tk.Label(title_frame, text="Windows AI Assistant",
                        bg=self.colors['bg_dark'], fg=self.colors['text'],
                        font=('Roboto', 20, 'bold'))
        title.pack(anchor=tk.W)
        
        subtitle = tk.Label(title_frame, text="Запуск приложений Windows 10 на Windows 7",
                           bg=self.colors['bg_dark'], fg=self.colors['text_muted'],
                           font=('Roboto', 10))
        subtitle.pack(anchor=tk.W)
        
    def create_chat_area(self, parent):
        chat_container = tk.Frame(parent, bg=self.colors['bg_dark'])
        chat_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        # Область сообщений
        chat_card = tk.Frame(chat_container, bg=self.colors['bg_card'],
                            highlightbackground=self.colors['border'],
                            highlightthickness=1)
        chat_card.pack(fill=tk.BOTH, expand=True)
        
        # Скролл для чата
        self.chat_display = scrolledtext.ScrolledText(
            chat_card,
            wrap=tk.WORD,
            bg=self.colors['bg_card'],
            fg=self.colors['text'],
            font=('Roboto', 10),
            padx=15,
            pady=15,
            borderwidth=0,
            highlightthickness=0
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        self.chat_display.config(state=tk.DISABLED)
        
        # Поле ввода
        input_frame = tk.Frame(chat_card, bg=self.colors['bg_card'], height=70)
        input_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=15, pady=15)
        input_frame.pack_propagate(False)
        
        self.input_field = tk.Entry(
            input_frame,
            bg=self.colors['bg_dark'],
            fg=self.colors['text'],
            font=('Roboto', 10),
            borderwidth=1,
            relief='solid',
            insertbackground=self.colors['text']
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        self.input_field.bind('<Return>', lambda e: self.send_message())
        
        send_btn = ttk.Button(input_frame, text="➤ Отправить",
                             style='Primary.TButton',
                             command=self.send_message)
        send_btn.pack(side=tk.RIGHT)
        
    def create_sidebar(self, parent):
        sidebar = tk.Frame(parent, bg=self.colors['bg_dark'], width=350)
        sidebar.pack(side=tk.RIGHT, fill=tk.Y)
        sidebar.pack_propagate(False)
        
        # Статус системы
        self.create_status_card(sidebar)
        
        # Быстрые действия
        self.create_actions_card(sidebar)
        
        # Недавние запуски
        self.create_recent_card(sidebar)
        
    def create_status_card(self, parent):
        card = tk.Frame(parent, bg=self.colors['bg_card'],
                       highlightbackground=self.colors['border'],
                       highlightthickness=1)
        card.pack(fill=tk.X, pady=(0, 15))
        
        header = tk.Label(card, text="📊 Статус системы",
                         bg=self.colors['bg_card'], fg=self.colors['text'],
                         font=('Roboto', 12, 'bold'))
        header.pack(anchor=tk.W, padx=15, pady=(15, 10))
        
        # Прогресс-бары
        self.create_progress_bar(card, "Совместимость", 75)
        self.create_progress_bar(card, "Обновления", 45)
        self.create_progress_bar(card, "Библиотеки", 90)
        
    def create_progress_bar(self, parent, label, value):
        container = tk.Frame(parent, bg=self.colors['bg_card'])
        container.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        # Заголовок и значение
        top_frame = tk.Frame(container, bg=self.colors['bg_card'])
        top_frame.pack(fill=tk.X, pady=(0, 5))
        
        tk.Label(top_frame, text=label, bg=self.colors['bg_card'],
                fg=self.colors['text_muted'], font=('Roboto', 9)).pack(side=tk.LEFT)
        
        tk.Label(top_frame, text=f"{value}%", bg=self.colors['bg_card'],
                fg=self.colors['primary'], font=('Roboto', 9, 'bold')).pack(side=tk.RIGHT)
        
        # Прогресс-бар
        progress_bg = tk.Frame(container, bg=self.colors['bg_dark'], height=8)
        progress_bg.pack(fill=tk.X)
        
        progress_fill = tk.Frame(progress_bg, bg=self.colors['primary'], height=8)
        progress_fill.place(x=0, y=0, relwidth=value/100, height=8)
        
    def create_actions_card(self, parent):
        card = tk.Frame(parent, bg=self.colors['bg_card'],
                       highlightbackground=self.colors['border'],
                       highlightthickness=1)
        card.pack(fill=tk.X, pady=(0, 15))
        
        header = tk.Label(card, text="⚡ Быстрые действия",
                         bg=self.colors['bg_card'], fg=self.colors['text'],
                         font=('Roboto', 12, 'bold'))
        header.pack(anchor=tk.W, padx=15, pady=(15, 10))
        
        actions = [
            ("📥 Установить обновления", self.install_updates),
            ("🛡️ Режим совместимости", self.compatibility_mode),
            ("🔄 Обновить библиотеки", self.update_libraries)
        ]
        
        for text, command in actions:
            btn = tk.Button(card, text=text,
                          bg=self.colors['bg_dark'],
                          fg=self.colors['text'],
                          font=('Roboto', 9),
                          borderwidth=1,
                          relief='solid',
                          activebackground=self.colors['border'],
                          activeforeground=self.colors['text'],
                          cursor='hand2',
                          anchor='w',
                          padx=10,
                          pady=8,
                          command=command)
            btn.pack(fill=tk.X, padx=15, pady=(0, 8))
            
        tk.Frame(card, height=10, bg=self.colors['bg_card']).pack()
        
    def create_recent_card(self, parent):
        card = tk.Frame(parent, bg=self.colors['bg_card'],
                       highlightbackground=self.colors['border'],
                       highlightthickness=1)
        card.pack(fill=tk.X)
        
        header = tk.Label(card, text="🕐 Недавние запуски",
                         bg=self.colors['bg_card'], fg=self.colors['text'],
                         font=('Roboto', 12, 'bold'))
        header.pack(anchor=tk.W, padx=15, pady=(15, 10))
        
        recent_apps = ["Discord.exe", "Telegram.exe", "Chrome 120"]
        
        for app in recent_apps:
            item = tk.Frame(card, bg=self.colors['bg_card'])
            item.pack(fill=tk.X, padx=15, pady=(0, 10))
            
            tk.Label(item, text="📦", bg=self.colors['bg_card'],
                    fg=self.colors['primary'], font=('Arial', 12)).pack(side=tk.LEFT, padx=(0, 8))
            
            tk.Label(item, text=app, bg=self.colors['bg_card'],
                    fg=self.colors['text'], font=('Roboto', 9)).pack(side=tk.LEFT)
            
            tk.Label(item, text="✓ Успешно", bg=self.colors['bg_card'],
                    fg=self.colors['accent'], font=('Roboto', 8)).pack(side=tk.RIGHT)
            
        tk.Frame(card, height=10, bg=self.colors['bg_card']).pack()
        
    def add_welcome_message(self):
        welcome = "Привет! Я помогу запустить приложения Windows 10 на твоей Windows 7. Что нужно сделать?"
        self.add_message("assistant", welcome)
        
    def add_message(self, role, text):
        self.chat_display.config(state=tk.NORMAL)
        
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        if role == "assistant":
            prefix = f"🤖 AI Assistant  {timestamp}\n"
            self.chat_display.insert(tk.END, prefix, 'assistant_name')
            self.chat_display.insert(tk.END, f"{text}\n\n", 'assistant_msg')
        else:
            prefix = f"👤 Вы  {timestamp}\n"
            self.chat_display.insert(tk.END, prefix, 'user_name')
            self.chat_display.insert(tk.END, f"{text}\n\n", 'user_msg')
        
        self.chat_display.tag_config('assistant_name',
                                    foreground=self.colors['primary'],
                                    font=('Roboto', 9, 'bold'))
        self.chat_display.tag_config('assistant_msg',
                                    foreground=self.colors['text'],
                                    font=('Roboto', 10))
        self.chat_display.tag_config('user_name',
                                    foreground=self.colors['accent'],
                                    font=('Roboto', 9, 'bold'))
        self.chat_display.tag_config('user_msg',
                                    foreground=self.colors['text'],
                                    font=('Roboto', 10))
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        
    def send_message(self):
        message = self.input_field.get().strip()
        if not message:
            return
            
        self.add_message("user", message)
        self.input_field.delete(0, tk.END)
        
        # Имитация ответа AI
        self.root.after(500, lambda: self.add_message(
            "assistant",
            "Анализирую приложение... Настраиваю параметры совместимости для запуска на Windows 7.\n\n"
            "✓ Проверка версии Windows\n"
            "✓ Установка недостающих библиотек\n"
            "✓ Настройка режима совместимости\n\n"
            "Готово! Приложение готово к запуску."
        ))
        
    def install_updates(self):
        messagebox.showinfo("Обновления", "Проверка доступных обновлений системы...")
        
    def compatibility_mode(self):
        messagebox.showinfo("Совместимость", "Включение режима совместимости Windows 10...")
        
    def update_libraries(self):
        messagebox.showinfo("Библиотеки", "Обновление системных библиотек...")


def main():
    root = tk.Tk()
    app = SberAIAssistant(root)
    
    # Центрирование окна
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()
