from models.student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        print("\n--- Thêm Sinh Viên Mới ---")
        sid = input("Nhập mã sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        age = input("Nhập tuổi: ")
        major = input("Nhập chuyên ngành: ")

        new_student = Student(sid, name, age, major)
        self.students.append(new_student)
        print("Thêm sinh viên thành công!")

    def show_all_students(self):
        print("\n--- Danh Sách Sinh Viên ---")
        if not self.students:
            print("Danh sách trống.")
        else:
            for st in self.students:
                print(st)

    def find_student_by_id(self):
        sid = input("\nNhập mã sinh viên cần tìm: ")
        for st in self.students:
            if st.student_id == sid:
                print(st)
                return
        print("Không tìm thấy sinh viên có mã này.")

    def delete_student(self):
        sid = input("\nNhập mã sinh viên cần xóa: ")
        for st in self.students:
            if st.student_id == sid:
                self.students.remove(st)
                print("Đã xóa sinh viên thành công.")
                return
        print("Không tìm thấy sinh viên để xóa.")
