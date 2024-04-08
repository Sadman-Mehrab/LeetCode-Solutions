class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        i = j = 0
        while i < len(students) and j < len(students) and sandwiches[i] in students[j:]:
            if sandwiches[i] == students[j]:
                count += 1
                i += 1
            else:
                students.append(students[j])
            j += 1
        return len(sandwiches) - count
