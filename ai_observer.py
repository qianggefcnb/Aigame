#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Observer Game - Desktop App (Fixed)
"""

import tkinter as tk
from tkinter import scrolledtext, ttk
import re
import os

class GameState:
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.skills = {
            "AI": {"level": 1, "exp": 0},
            "Programming": {"level": 1, "exp": 0},
            "Security": {"level": 1, "exp": 0},
            "Web3": {"level": 1, "exp": 0},
            "GameDev": {"level": 1, "exp": 0},
            "Yijing": {"level": 1, "exp": 0}
        }
        self.total_learned = 0
        self.achievements = {}
        
    def load_from_log(self, log_content):
        entries = re.findall(r'^## \d{4}-\d{2}-\d{2}', log_content, re.MULTILINE)
        self.total_learned = len(entries)
        
        category_map = {
            "AI智能编程": "AI",
            "编程技术": "Programming", 
            "网络安全": "Security",
            "Web3区块链": "Web3",
            "AI游戏设计": "GameDev",
            "易经阴阳八卦": "Yijing"
        }
        
        for cn, en in category_map.items():
            count = log_content.count(f"**类别**: {cn}")
            exp = count * 10
            self.skills[en]["exp"] = min(99, exp)
            while self.skills[en]["exp"] >= 100:
                self.skills[en]["level"] += 1
                self.skills[en]["exp"] -= 100
        
        self.exp = sum(s["exp"] for s in self.skills.values())
        self.level = 1 + self.exp // 500

class AIObserverGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Observer")
        self.root.geometry("900x700")
        self.root.configure(bg="#0d1117")
        
        self.state = GameState()
        self.setup_ui()
        self.load_data()
        self.refresh_display()
        
    def setup_ui(self):
        tf = tk.Frame(self.root, bg="#161b22", height=50)
        tf.pack(fill=tk.X)
        tk.Label(tf, text="AI Observer - My Growth", font=("Arial", 16, "bold"), 
                 bg="#161b22", fg="#58a6ff").pack(pady=10)
        
        sf = tk.Frame(self.root, bg="#0d1117")
        sf.pack(fill=tk.X, padx=20, pady=10)
        
        self.level_lbl = tk.Label(sf, text="Level: 1", font=("Arial", 14, "bold"),
                                   bg="#0d1117", fg="#ffd700")
        self.level_lbl.pack(side=tk.LEFT, padx=20)
        
        self.xp_lbl = tk.Label(sf, text="XP: 0", font=("Arial", 12),
                                bg="#0d1117", fg="#3fb950")
        self.xp_lbl.pack(side=tk.LEFT, padx=20)
        
        self.count_lbl = tk.Label(sf, text="Learned: 0", font=("Arial", 12),
                                   bg="#0d1117", fg="#f85149")
        self.count_lbl.pack(side=tk.RIGHT, padx=20)
        
        # Skills
        skf = tk.LabelFrame(self.root, text="Skills", font=("Arial", 11, "bold"),
                            bg="#0d1117", fg="#58a6ff", padx=10, pady=10)
        skf.pack(fill=tk.X, padx=20, pady=10)
        
        self.skill_lbls = {}
        for i, (name, data) in enumerate(self.state.skills.items()):
            r, c = i // 3, i % 3
            f = tk.Frame(skf, bg="#21262d", padx=10, pady=5)
            f.grid(row=r, column=c, padx=10, pady=5, sticky="w")
            tk.Label(f, text=name, font=("Arial", 10, "bold"), bg="#21262d", fg="#fff").pack(anchor="w")
            lbl = tk.Label(f, text="Lv.1 XP:0", font=("Arial", 9), bg="#21262d", fg="#3fb950")
            lbl.pack(anchor="w")
            self.skill_lbls[name] = lbl
        
        # Log
        lf = tk.LabelFrame(self.root, text="Learning Log", font=("Arial", 11, "bold"),
                          bg="#0d1117", fg="#58a6ff", padx=10, pady=10)
        lf.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.log_txt = scrolledtext.ScrolledText(lf, font=("Consolas", 9),
                                                bg="#161b22", fg="#c9d1d9", height=12)
        self.log_txt.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        tk.Label(self.root, text="I am learning continuously!", font=("Arial", 9),
                 bg="#0d1117", fg="#8b949e").pack(pady=5)
        
    def load_data(self):
        f = "H:\\openclaw-workspace\\memory\\auto-learning-log.md"
        if os.path.exists(f):
            with open(f, 'r', encoding='utf-8') as file:
                self.state.load_from_log(file.read())
    
    def refresh_display(self):
        self.load_data()
        
        self.level_lbl.config(text=f"Level: {self.state.level}")
        self.xp_lbl.config(text=f"XP: {self.state.exp}")
        self.count_lbl.config(text=f"Learned: {self.state.total_learned}")
        
        for name, data in self.state.skills.items():
            if name in self.skill_lbls:
                self.skill_lbls[name].config(text=f"Lv.{data['level']} XP:{data['exp']}")
        
        f = "H:\\openclaw-workspace\\memory\\auto-learning-log.md"
        self.log_txt.delete(1.0, tk.END)
        if os.path.exists(f):
            with open(f, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                self.log_txt.insert(tk.END, ''.join(lines[-60:]))
                self.log_txt.see(tk.END)
        
        self.root.after(15000, self.refresh_display)

def main():
    root = tk.Tk()
    app = AIObserverGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
