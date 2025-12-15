export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter(element => element.location === city)
    .map(element => {
      const gradeObj = newGrades.find(g => g.studentId === element.id);
      return {
        ...element,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}
