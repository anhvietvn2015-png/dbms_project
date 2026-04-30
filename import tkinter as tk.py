import customtkinter as ctk # Thư viện UI hiện đại
from tkinter import messagebox

# Cấu hình giao diện (Màu sắc lấy cảm hứng từ Stitch)
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 

class SalesAppModern:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Management System")
        self.root.geometry("1100x700")

        # --- LAYOUT CHÍNH ---
        # Sidebar màu tối theo Stitch
        self.sidebar = ctk.CTkFrame(self.root, width=240, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.logo_label = ctk.CTkLabel(self.sidebar, text="GROUP 1", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=30)

        # Content area
        self.main_view = ctk.CTkFrame(self.root, corner_radius=20)
        self.main_view.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # --- NAVIGATION BUTTONS (M4 Design) ---
        self.btn_customer = ctk.CTkButton(self.sidebar, text="Khách hàng", 
                                          command=self.show_customer_form,
                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                          hover_color="#34495e")
        self.btn_customer.pack(fill="x", padx=20, pady=10)

        self.btn_order = ctk.CTkButton(self.sidebar, text="Đơn hàng", 
                                       command=lambda: print("Chuyển sang Đơn hàng"))
        self.btn_order.pack(fill="x", padx=20, pady=10)

        self.show_customer_form()

    def show_customer_form(self):
        # Clear main view
        for widget in self.main_view.winfo_children():
            widget.destroy()

        # Header lấy từ thiết kế Stitch
        title = ctk.CTkLabel(self.main_view, text="Đăng ký Khách hàng mới", 
                             font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=(40, 20))

        # Form container
        form_container = ctk.CTkFrame(self.main_view, fg_color="transparent")
        form_container.pack(pady=20)

        # Các trường nhập liệu bo tròn (Style Stitch)
        self.name_entry = ctk.CTkEntry(form_container, placeholder_text="Tên khách hàng", width=350, height=45)
        self.name_entry.pack(pady=10)

        self.email_entry = ctk.CTkEntry(form_container, placeholder_text="Email liên hệ", width=350, height=45)
        self.email_entry.pack(pady=10)

        self.phone_entry = ctk.CTkEntry(form_container, placeholder_text="Số điện thoại", width=350, height=45)
        self.phone_entry.pack(pady=10)

        # Nút xác nhận nổi bật
        btn_save = ctk.CTkButton(form_container, text="Lưu thông tin", 
                                 width=350, height=50, corner_radius=10,
                                 command=self.handle_save)
        btn_save.pack(pady=30)

    def handle_save(self):
        # Giữ nguyên logic validation của bạn
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Lỗi", "Vui lòng nhập tên!")
        else:
            messagebox.showinfo("Thành công", f"Đã lưu {name}")

if __name__ == "__main__":
    app_root = ctk.CTk()
    app = SalesAppModern(app_root)
    app_root.mainloop()