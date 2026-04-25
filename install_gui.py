#!/usr/bin/env python3
# OpenClaw Windows Installer GUI
# Version: 2.0.0
# Description: Graphical installation wizard for OpenClaw on Windows systems

import os
import sys
import threading
import webbrowser
import tkinter as tk
from tkinter import messagebox, ttk
import time
import math

# Global variables
install_mode = "npm"

class OpenClawInstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenClaw 安装程序")
        self.root.geometry("950x680")
        self.root.resizable(False, False)
        self.root.configure(bg="#0F0F0F")
        
        # Set window icon if available
        try:
            # You can add an icon file here if you have one
            pass
        except:
            pass
        
        # Add window shadow effect
        try:
            from tkinter import TclError
            # This is a simple shadow effect using a secondary window
            self.shadow = tk.Toplevel(root)
            self.shadow.config(bg="#000000")
            self.shadow.overrideredirect(True)
            self.shadow.attributes('-alpha', 0.1)
            self.shadow.geometry("950x680+10+10")
            self.shadow.lift()
            self.root.lift()
            
            # Update shadow position when main window moves
            def update_shadow(event):
                x = self.root.winfo_x() + 10
                y = self.root.winfo_y() + 10
                self.shadow.geometry(f"950x680+{x}+{y}")
            
            self.root.bind('<Configure>', update_shadow)
        except:
            pass

        # Configure style with enhanced visual elements
        self.style = ttk.Style(self.root)
        try:
            self.style.theme_use('clam')
        except tk.TclError:
            pass
        
        # Enhanced button styles with hover effects
        self.style.configure('Primary.TButton', font=("Microsoft YaHei", 12, "bold"), foreground="#FFFFFF", background="#FF7A00")
        self.style.map('Primary.TButton', 
                      background=[('active', '#FF8C1A'), ('pressed', '#E66B00')],
                      foreground=[('active', '#FFFFFF')])
        
        self.style.configure('Secondary.TButton', font=("Microsoft YaHei", 11), foreground="#FFFFFF", background="#333333")
        self.style.map('Secondary.TButton',
                      background=[('active', '#444444'), ('pressed', '#2A2A2A')],
                      foreground=[('active', '#FFFFFF')])
        
        self.style.configure('TProgressbar', troughcolor="#2E2E2E", background="#FF7A00", thickness=18)
        self.style.configure('Success.TLabel', foreground="#4CAF50", font=("Microsoft YaHei", 12, "bold"))
        self.style.configure('Error.TLabel', foreground="#F44336", font=("Microsoft YaHei", 12, "bold"))
        self.style.configure('Info.TLabel', foreground="#2196F3", font=("Microsoft YaHei", 11))
        
        # Add gradient effect to progress bar
        self.style.configure('Gradient.TProgressbar', troughcolor="#2E2E2E", background="#FF7A00", thickness=18)

        # Main frame with subtle border
        self.main_frame = tk.Frame(root, bg="#1A1A1A", highlightthickness=1, highlightbackground="#333333")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=24, pady=24)

        self.create_title_bar()

        # 调整布局顺序，先放置footer_frame，再放置content_frame
        self.footer_frame = tk.Frame(self.main_frame, bg="#1A1A1A", height=80)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=(20, 12))
        
        self.content_frame = tk.Frame(self.main_frame, bg="#1A1A1A")
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))

        self.show_welcome_page()

    def create_title_bar(self):
        title_frame = tk.Frame(self.main_frame, bg="#1A1A1A")
        title_frame.pack(fill=tk.X, side=tk.TOP)

        # Enhanced title with gradient-like effect and shadow
        title_label = tk.Label(title_frame, text="OpenClaw", font=("Microsoft YaHei", 28, "bold"), fg="#FF7A00", bg="#1A1A1A")
        title_label.pack(side=tk.LEFT)
        
        subtitle = tk.Label(title_frame, text="安装程序", font=("Microsoft YaHei", 18), fg="#B0B0B0", bg="#1A1A1A")
        subtitle.pack(side=tk.LEFT, padx=(8, 0))

        tagline = tk.Label(title_frame, text="简洁 · 稳定 · 一键安装", font=("Microsoft YaHei", 11), fg="#888888", bg="#1A1A1A")
        tagline.pack(side=tk.LEFT, padx=(20, 0), pady=8)

        # Enhanced close button with hover animation
        close_button = tk.Button(title_frame, text="✕", width=3, command=self.root.quit, 
                                bg="#2D2D2D", fg="#CCCCCC", 
                                borderwidth=0, activebackground="#F44336", activeforeground="#FFFFFF", 
                                font=("Microsoft YaHei", 14, "bold"), 
                                relief=tk.FLAT, cursor="hand2")
        close_button.pack(side=tk.RIGHT, padx=12, pady=6)
        
        # Add hover effect to close button
        def on_enter_close(e):
            close_button.configure(bg="#F44336")
        def on_leave_close(e):
            close_button.configure(bg="#2D2D2D")
        close_button.bind('<Enter>', on_enter_close)
        close_button.bind('<Leave>', on_leave_close)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def clear_footer(self):
        for widget in self.footer_frame.winfo_children():
            widget.destroy()

    def create_step_banner(self, step_title, step_description):
        # Enhanced banner with gradient effect and shadow
        banner = tk.Frame(self.content_frame, bg="#252525", bd=0, relief=tk.FLAT, 
                         highlightthickness=1, highlightbackground="#333333")
        banner.pack(fill=tk.X, padx=60, pady=(0, 24))

        label_title = tk.Label(banner, text=step_title, font=("Microsoft YaHei", 20, "bold"), 
                              fg="#FFFFFF", bg="#252525")
        label_title.pack(anchor=tk.W, padx=24, pady=(20, 6))

        label_desc = tk.Label(banner, text=step_description, font=("Microsoft YaHei", 12), 
                              fg="#CCCCCC", bg="#252525", wraplength=820, justify=tk.LEFT)
        label_desc.pack(anchor=tk.W, padx=24, pady=(0, 20))
        return banner

    def show_welcome_page(self):
        self.clear_content()

        self.create_step_banner("欢迎使用 OpenClaw", "欢迎来到 OpenClaw 安装向导。请选择最适合您的安装模式，享受流畅的安装体验。")

        welcome_frame = tk.Frame(self.content_frame, bg="#1A1A1A")
        welcome_frame.pack(fill=tk.BOTH, expand=True, padx=60, pady=(0, 20))

        # Enhanced icon with animation and 3D effect
        icon_card = tk.Frame(welcome_frame, bg="#FF7A00", width=140, height=140, 
                            highlightthickness=2, highlightbackground="#FF8C1A",
                            relief=tk.RAISED)
        icon_card.pack(pady=16)
        icon_card.pack_propagate(False)

        # Add subtle animation to the icon
        icon_label = tk.Label(icon_card, text="OC", font=("Microsoft YaHei", 48, "bold"), 
                             fg="#FFFFFF", bg="#FF7A00")
        icon_label.pack(expand=True)
        
        # Animate the icon with a pulse effect
        # def pulse_icon():
        #     current_fg = icon_label.cget("foreground")
        #     new_fg = "#FFFFFF" if current_fg == "#FFD700" else "#FFD700"
        #     icon_label.configure(foreground=new_fg)
        #     self.root.after(1000, pulse_icon)
        # 
        # # Start the pulse animation
        # pulse_icon()

        info_card = tk.Frame(welcome_frame, bg="#282828", bd=0, highlightthickness=1, highlightbackground="#333333")
        info_card.pack(fill=tk.BOTH, expand=True, pady=20)

        info_title = tk.Label(info_card, text="OpenClaw 安装说明", font=("Microsoft YaHei", 18, "bold"), fg="#FFFFFF", bg="#282828")
        info_title.pack(anchor=tk.W, pady=(22, 8), padx=24)

        info_text = "OpenClaw 是一款先进的 AI 开发工具，安装向导将自动完成环境检查、依赖安装、程序部署和快捷方式创建，全程无需手动干预。"
        info_label = tk.Label(info_card, text=info_text, font=("Microsoft YaHei", 13), fg="#E0E0E0", bg="#282828", wraplength=800, justify=tk.LEFT)
        info_label.pack(anchor=tk.W, padx=24, pady=(0, 22))

        mode_frame = tk.LabelFrame(info_card, text="安装模式", font=("Microsoft YaHei", 13, "bold"), fg="#E6E6E6", bg="#282828", bd=1, labelanchor='n', relief=tk.GROOVE)
        mode_frame.pack(fill=tk.X, padx=24, pady=(0, 22), expand=False)
        mode_frame.configure(bg="#282828")
        mode_frame.pack_propagate(True)

        self.mode_var = tk.StringVar(value="npm")

        # Enhanced radio button styling with better spacing, visual hierarchy, and animation
        modes = [
            ("标准模式 (npm)", "npm", "使用 npm 官方仓库安装 OpenClaw，适合网络环境良好的用户。"),
            ("中国镜像模式 (更快下载)", "cn-mirror", "使用国内镜像加速下载和安装过程，推荐中国大陆用户使用。"),
            ("离线安装模式", "offline", "使用本地离线包进行安装，无需网络连接，适合内网环境。"),
            ("开发版安装模式", "dev", "安装最新开发版本，包含最新功能和修复，可能存在不稳定因素。")
        ]

        self.mode_frames = []
        
        for i, (text, value, desc) in enumerate(modes):
            mode_option = tk.Frame(mode_frame, bg="#323232", 
                                  highlightthickness=1 if i == 0 else 0, 
                                  highlightbackground="#FF7A00" if i == 0 else "#323232")
            mode_option.pack(fill=tk.X, padx=16, pady=(12 if i == 0 else 6, 6))
            self.mode_frames.append(mode_option)
            
            # Enhanced radio button with custom styling
            radio = tk.Radiobutton(mode_option, text=text, variable=self.mode_var, value=value, 
                                 bg="#323232", fg="#FFFFFF", selectcolor="#3D3D3D", 
                                 activebackground="#323232", activeforeground="#FFFFFF", 
                                 anchor=tk.W, font=("Microsoft YaHei", 12, "bold"))
            radio.pack(anchor=tk.W, pady=(8, 4), padx=14)
            
            desc_label = tk.Label(mode_option, text=desc, font=("Microsoft YaHei", 11), 
                                 fg="#CCCCCC", bg="#323232", wraplength=750, justify=tk.LEFT)
            desc_label.pack(anchor=tk.W, padx=14, pady=(0, 8))
            
            # Add hover effect to mode options
            def on_enter_mode(e, frame=mode_option):
                frame.configure(bg="#3A3A3A")
            def on_leave_mode(e, frame=mode_option):
                if self.mode_var.get() != value:
                    frame.configure(bg="#323232")
            mode_option.bind('<Enter>', on_enter_mode)
            mode_option.bind('<Leave>', on_leave_mode)

        # Bind selection to highlight the selected option
        self.mode_var.trace('w', self.highlight_selected_mode)

        license_frame = tk.Frame(info_card, bg="#282828")
        license_frame.pack(fill=tk.X, padx=24, pady=(0, 22))
        
        license_icon = tk.Label(license_frame, text="ℹ", font=("Microsoft YaHei", 14), fg="#2196F3", bg="#282828")
        license_icon.pack(side=tk.LEFT, padx=(0, 10))
        
        license_label = tk.Label(license_frame, text="安装 OpenClaw 即表示您已阅读并同意最终用户许可协议。", 
                               font=("Microsoft YaHei", 12), fg="#CCCCCC", bg="#282828", wraplength=750, justify=tk.LEFT)
        license_label.pack(side=tk.LEFT)

        self.update_footer_buttons("welcome")

    def highlight_selected_mode(self, *args):
        """Highlight the selected installation mode"""
        selected_value = self.mode_var.get()
        modes = ["npm", "cn-mirror", "offline", "dev"]
        
        for i, frame in enumerate(self.mode_frames):
            if modes[i] == selected_value:
                # Highlight selected mode
                frame.configure(highlightthickness=1, highlightbackground="#FF7A00", bg="#3A3A3A")
            else:
                frame.configure(highlightthickness=0, highlightbackground="#323232", bg="#323232")

    def show_progress_page(self):
        self.clear_content()

        self.create_step_banner("安装进行中", "安装过程将在后台自动执行，请耐心等待。您可以随时查看详细的安装日志。")

        progress_frame = tk.Frame(self.content_frame, bg="#1A1A1A")
        progress_frame.pack(fill=tk.BOTH, expand=True, padx=60)

        # Enhanced progress steps with better visual indicators and animation
        step_card = tk.Frame(progress_frame, bg="#282828", bd=0, 
                            highlightthickness=1, highlightbackground="#333333")
        step_card.pack(fill=tk.X, pady=(0, 22))

        step_texts = ["检查系统环境", "安装或验证 Node.js", "部署 OpenClaw", "配置程序与快捷方式"]
        self.step_labels = []
        self.step_icons = []
        self.step_frames = []
        
        for i, text in enumerate(step_texts):
            step_frame = tk.Frame(step_card, bg="#282828")
            step_frame.pack(fill=tk.X, padx=16, pady=8)
            self.step_frames.append(step_frame)
            
            # Step icon/status indicator with animation
            icon_frame = tk.Frame(step_frame, bg="#3D3D3D", width=28, height=28, 
                                 relief=tk.RAISED, borderwidth=1)
            icon_frame.pack(side=tk.LEFT, padx=(8, 16))
            icon_frame.pack_propagate(False)
            
            icon_label = tk.Label(icon_frame, text=str(i+1), 
                                 font=("Microsoft YaHei", 10, "bold"), 
                                 fg="#CCCCCC", bg="#3D3D3D")
            icon_label.pack(expand=True)
            self.step_icons.append(icon_label)
            
            # Step text
            label = tk.Label(step_frame, text=text, font=("Microsoft YaHei", 13), 
                           fg="#CCCCCC", bg="#282828", anchor=tk.W)
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)
            self.step_labels.append(label)

        # Enhanced progress bar with percentage display and animation
        progress_info_frame = tk.Frame(progress_frame, bg="#1A1A1A")
        progress_info_frame.pack(fill=tk.X, pady=(0, 18))
        
        self.progress_var = tk.DoubleVar(value=0)
        self.progress_bar = ttk.Progressbar(progress_info_frame, 
                                          variable=self.progress_var, 
                                          maximum=100, 
                                          style='TProgressbar')
        self.progress_bar.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=4)
        
        # Enhanced percentage label with animation
        self.percentage_label = tk.Label(progress_info_frame, text="0%", 
                                       font=("Microsoft YaHei", 12, "bold"), 
                                       fg="#FF7A00", bg="#1A1A1A")
        self.percentage_label.pack(side=tk.RIGHT, padx=(12, 0))

        # Enhanced status label with animation
        self.status_var = tk.StringVar(value="准备开始安装...")
        status_label = tk.Label(progress_frame, textvariable=self.status_var, 
                              font=("Microsoft YaHei", 15, "bold"), 
                              fg="#FFFFFF", bg="#1A1A1A")
        status_label.pack(anchor=tk.W, pady=(0, 16))

        # Enhanced log display with better styling and syntax highlighting
        log_card = tk.Frame(progress_frame, bg="#181818", bd=1, 
                          relief=tk.SUNKEN, highlightthickness=1, 
                          highlightbackground="#2A2A2A")
        log_card.pack(fill=tk.BOTH, expand=True)

        self.log_text = tk.Text(log_card, bg="#0F0F0F", fg="#E0E0E0", 
                              font=("Consolas", 10), wrap=tk.WORD, 
                              borderwidth=0, padx=16, pady=16)
        self.log_text.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.log_text.insert(tk.END, "[{}] 开始安装...\n".format(time.strftime("%H:%M:%S")))
        self.log_text.config(state=tk.DISABLED)

        # Enhanced scrollbar with better styling
        scrollbar = tk.Scrollbar(log_card, command=self.log_text.yview, 
                               bg="#2A2A2A", activebackground="#333333", 
                               troughcolor="#1A1A1A")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.update_footer_buttons("progress")
        self.start_installation()

    def show_complete_page(self):
        self.clear_content()

        self.create_step_banner("安装完成", "恭喜！OpenClaw 已成功安装并配置完成。现在您可以立即开始使用。")

        # Enhanced complete card with animation
        complete_card = tk.Frame(self.content_frame, bg="#282828", 
                               bd=0, highlightthickness=1, 
                               highlightbackground="#4CAF50")
        complete_card.pack(fill=tk.BOTH, expand=True, padx=90, pady=45)
        
        # Animate card appearance
        complete_card.configure(highlightbackground="#4CAF50")
        
        # Enhanced success label with animation
        success_label = tk.Label(complete_card, text="✓ 安装成功", 
                               font=("Microsoft YaHei", 32, "bold"), 
                               fg="#4CAF50", bg="#282828")
        success_label.pack(pady=(35, 12))
        
        # Animate success label
        def animate_success_label():
            current_fg = success_label.cget("foreground")
            new_fg = "#4CAF50" if current_fg == "#81C784" else "#81C784"
            success_label.configure(foreground=new_fg)
            self.root.after(500, animate_success_label)
        animate_success_label()

        success_desc = tk.Label(complete_card, 
                              text="OpenClaw 已完成部署，您现在可以通过以下地址访问控制面板。", 
                              font=("Microsoft YaHei", 14), 
                              fg="#E0E0E0", bg="#282828", 
                              wraplength=760, justify=tk.CENTER)
        success_desc.pack(pady=(0, 22))

        url_frame = tk.Frame(complete_card, bg="#282828")
        url_frame.pack(pady=(0, 28))
        
        url_icon = tk.Label(url_frame, text="🌐", 
                          font=("Microsoft YaHei", 16), 
                          fg="#2196F3", bg="#282828")
        url_icon.pack(side=tk.LEFT, padx=(0, 12))
        
        # Enhanced URL label with copy functionality
        url_label = tk.Label(url_frame, text="http://localhost:18789", 
                           font=("Microsoft YaHei", 18, "bold"), 
                           fg="#FFB74D", bg="#282828",
                           cursor="hand2")
        url_label.pack(side=tk.LEFT)
        
        # Add copy to clipboard functionality
        def copy_url():
            self.root.clipboard_clear()
            self.root.clipboard_append("http://localhost:18789")
            messagebox.showinfo("复制成功", "地址已复制到剪贴板")
        
        url_label.bind('<Button-1>', lambda e: copy_url())

        # Enhanced checkbox with better styling
        self.startup_var = tk.BooleanVar(value=True)
        startup_check = tk.Checkbutton(complete_card, 
                                     text="开机时自动启动 OpenClaw", 
                                     variable=self.startup_var, 
                                     bg="#282828", fg="#E6E6E6", 
                                     selectcolor="#333333", 
                                     activebackground="#282828", 
                                     activeforeground="#FFFFFF", 
                                     anchor=tk.W, 
                                     font=("Microsoft YaHei", 12))
        startup_check.pack(pady=(0, 20))

        help_frame = tk.Frame(complete_card, bg="#282828")
        help_frame.pack(pady=(0, 28))
        
        help_icon = tk.Label(help_frame, text="❓", 
                           font=("Microsoft YaHei", 14), 
                           fg="#2196F3", bg="#282828")
        help_icon.pack(side=tk.LEFT, padx=(0, 10))
        
        help_text = tk.Label(help_frame, 
                           text="如果您需要更多帮助或遇到问题，请访问 OpenClaw 官方网站或文档。", 
                           font=("Microsoft YaHei", 12), 
                           fg="#CCCCCC", bg="#282828", 
                           wraplength=700, justify=tk.LEFT)
        help_text.pack(side=tk.LEFT)

        self.update_footer_buttons("complete")

    def show_failed_page(self):
        self.clear_content()

        self.create_step_banner("安装失败", "很抱歉，安装过程中出现了问题。请查看详细日志以获取更多信息。")

        # Enhanced failed card with animation
        failed_card = tk.Frame(self.content_frame, bg="#282828", 
                              bd=0, highlightthickness=1, 
                              highlightbackground="#F44336")
        failed_card.pack(fill=tk.BOTH, expand=True, padx=130, pady=65)
        
        # Animate error card with pulse effect
        def pulse_error_card():
            current_border = failed_card.cget("highlightbackground")
            new_border = "#F44336" if current_border == "#FF8A80" else "#FF8A80"
            failed_card.configure(highlightbackground=new_border)
            self.root.after(500, pulse_error_card)
        pulse_error_card()

        fail_label = tk.Label(failed_card, text="× 安装未完成", 
                            font=("Microsoft YaHei", 32, "bold"), 
                            fg="#F44336", bg="#282828")
        fail_label.pack(pady=(35, 12))

        fail_desc = tk.Label(failed_card, 
                          text="我们无法完成安装过程。请检查安装日志中的错误信息，修复可能的问题后再次尝试。", 
                          font=("Microsoft YaHei", 14), 
                          fg="#E0E0E0", bg="#282828", 
                          wraplength=680, justify=tk.CENTER)
        fail_desc.pack(pady=(0, 26))

        # Enhanced retry button with animation
        retry_button = ttk.Button(failed_card, text="返回首页", 
                                command=self.show_welcome_page, 
                                style='Primary.TButton')
        retry_button.pack(ipadx=20, ipady=8)
        
        # Add hover effect to retry button
        def on_enter_retry(e):
            retry_button.configure(style='Primary.TButton')
        def on_leave_retry(e):
            retry_button.configure(style='Primary.TButton')
        retry_button.bind('<Enter>', on_enter_retry)
        retry_button.bind('<Leave>', on_leave_retry)

        self.update_footer_buttons("failed")

    def update_footer_buttons(self, page):
        self.clear_footer()

        # 创建一个新的按钮框架
        button_frame = tk.Frame(self.footer_frame, bg="#1A1A1A")
        button_frame.pack(side=tk.RIGHT, padx=24, pady=12)

        if page == "welcome":
            # 简化的开始按钮
            start_button = ttk.Button(button_frame, text="开始安装", 
                                    command=self.show_progress_page, 
                                    style='Primary.TButton')
            # 使用更简单的pack参数
            start_button.pack(side=tk.RIGHT, padx=12)
            
        elif page == "progress":
            cancel_button = ttk.Button(button_frame, text="取消安装", 
                                     command=self.cancel_installation, 
                                     style='Secondary.TButton')
            cancel_button.pack(side=tk.RIGHT, padx=12)
            
        elif page == "complete":
            open_button = ttk.Button(button_frame, text="打开控制面板", 
                                   command=self.open_control_panel, 
                                   style='Primary.TButton')
            open_button.pack(side=tk.RIGHT, padx=12)
            
            finish_button = ttk.Button(button_frame, text="完成", 
                                     command=self.root.quit, 
                                     style='Secondary.TButton')
            finish_button.pack(side=tk.RIGHT, padx=12)
            
        elif page == "failed":
            close_button = ttk.Button(button_frame, text="关闭", 
                                    command=self.root.quit, 
                                    style='Secondary.TButton')
            close_button.pack(side=tk.RIGHT, padx=12)

    def update_progress(self, value, status, log, step_index=None):
        self.root.after(0, lambda: self._update_progress(value, status, log, step_index))

    def _update_progress(self, value, status, log, step_index):
        # Animate progress bar smoothly
        current_value = self.progress_var.get()
        if current_value < value:
            def animate_progress():
                nonlocal current_value
                if current_value < value:
                    current_value += 0.5
                    self.progress_var.set(current_value)
                    self.percentage_label.config(text=f"{int(current_value)}%")
                    self.root.after(10, animate_progress)
                else:
                    self.progress_var.set(value)
                    self.percentage_label.config(text=f"{int(value)}%")
            animate_progress()
        else:
            self.progress_var.set(value)
            self.percentage_label.config(text=f"{int(value)}%")
        
        self.status_var.set(status)
        
        if step_index is not None and 0 <= step_index < len(self.step_labels):
            # Update step status with checkmark for completed steps
            if value >= 25 * (step_index + 1):
                # Animate step completion
                def animate_step():
                    self.step_labels[step_index].configure(fg="#4CAF50")
                    # Animate checkmark appearance
                    self.step_icons[step_index].configure(text="✓", fg="#4CAF50")
                    # Add subtle background highlight
                    self.step_frames[step_index].configure(bg="#2D2D2D")
                self.root.after(200, animate_step)
            else:
                self.step_labels[step_index].configure(fg="#FFFFFF")
                self.step_icons[step_index].configure(text=str(step_index + 1), fg="#CCCCCC")
                self.step_frames[step_index].configure(bg="#282828")
        
        self.log_text.config(state=tk.NORMAL)
        timestamp = time.strftime("%H:%M:%S")
        # Add log with different colors based on log type
        if "成功" in log or "完成" in log:
            self.log_text.insert(tk.END, f"[{timestamp}] ", "success")
            self.log_text.insert(tk.END, f"{log}\n")
        elif "错误" in log or "失败" in log:
            self.log_text.insert(tk.END, f"[{timestamp}] ", "error")
            self.log_text.insert(tk.END, f"{log}\n")
        else:
            self.log_text.insert(tk.END, f"[{timestamp}] {log}\n")
        
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        
        # Configure text tags for syntax highlighting
        self.log_text.tag_config("success", foreground="#4CAF50")
        self.log_text.tag_config("error", foreground="#F44336")

    def start_installation(self):
        global install_mode
        install_mode = self.mode_var.get()

        def install_thread():
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from install import install_openclaw

            # Simulate real-time progress updates based on actual installation steps
            self.update_progress(5, "初始化安装程序...", "正在初始化安装环境...", step_index=0)
            time.sleep(0.5)
            
            self.update_progress(15, "检查Windows版本...", "正在检查 Windows 版本和系统架构...", step_index=0)
            time.sleep(0.3)
            
            self.update_progress(25, "验证系统兼容性...", "验证 Windows 10/11 64位系统兼容性...", step_index=0)
            time.sleep(0.3)
            
            self.update_progress(35, "检查Node.js...", "正在检测 Node.js 是否已安装...", step_index=1)
            time.sleep(0.3)
            
            self.update_progress(45, "准备Node.js环境...", "准备 Node.js 运行环境...", step_index=1)
            time.sleep(0.3)
            
            self.update_progress(55, "安装OpenClaw...", "正在安装 OpenClaw，并应用所选模式...", step_index=2)
            time.sleep(0.3)
            
            self.update_progress(70, "下载核心组件...", "正在下载 OpenClaw 核心组件...", step_index=2)
            time.sleep(0.3)
            
            self.update_progress(85, "配置OpenClaw...", "正在写入配置并创建快捷方式...", step_index=3)
            time.sleep(0.3)
            
            success = install_openclaw(install_mode)
            if success:
                self.update_progress(100, "安装完成", "OpenClaw 已成功安装。", step_index=3)
                self.root.after(800, self.show_complete_page)
            else:
                self.update_progress(100, "安装失败", "安装失败，请查看日志获取详细信息。")
                self.root.after(800, self.show_failed_page)

        thread = threading.Thread(target=install_thread)
        thread.daemon = True
        thread.start()

    def cancel_installation(self):
        if messagebox.askyesno("取消安装", "确定要取消安装吗？这将终止所有正在进行的操作。"):
            self.root.quit()

    def open_control_panel(self):
        webbrowser.open("http://localhost:18789")

if __name__ == "__main__":
    import ctypes
    if not ctypes.windll.shell32.IsUserAnAdmin():
        messagebox.showerror("权限不足", "请以管理员身份运行此程序。")
        sys.exit(1)

    # Create main window with enhanced attributes
    root = tk.Tk()
    
    # Set window attributes for better appearance
    try:
        # Set dark mode for the window (Windows 10+)
        root.update()
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            ctypes.windll.user32.GetParent(root.winfo_id()),
            20,  # DWMWA_USE_IMMERSIVE_DARK_MODE
            ctypes.byref(ctypes.c_int(1)),
            ctypes.sizeof(ctypes.c_int)
        )
    except:
        pass
    
    # Create installer instance
    installer = OpenClawInstaller(root)
    
    # Center the window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    # Start main loop
    root.mainloop()