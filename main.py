from modules.function import StudentManager


def main_menu():
    sm = StudentManager()
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ SINH VIÊN =====")
        print("1. Xem danh sách sinh viên")
        print("2. Thêm sinh viên mới")
        print("3. Tìm kiếm sinh viên theo ID")
        print("4. Xóa sinh viên theo ID")
        print("5. Thoát chương trình")
        choice = input("Lựa chọn của bạn (1-5): ")
        if choice == '1':
            sm.show_all_student()
        elif choice == '2':
            sm.add_student()
        elif choice == '3':
            sm.find_student_by_id()
        elif choice == '4':
            sm.delete_student_by_id()
        elif choice == '5':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main_menu()
