import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import CourseCard from './CourseCard'; 
import './CourseListPage.css'; 

const CourseListPage = () => {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    getCourses();
  }, []);

  const getCourses = async () => {
    try {
      const response = await fetch('/api/courses/');
      const data = await response.json();
      setCourses(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className='pt-16 pb-12 relative bg-gray-200'>
      <div className='w-[80%] pt-8 pb-8 mx-auto'>
        <h1 className='text-4xl md:text-5xl text-gray-900 font-bold'>Available Courses</h1>
        <div className='md:mt-16 mt-10 grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-10'>
          {courses.map((course) => (
            <Link key={course.id} to={`/course/${course.id}`} className="course-link">
              <CourseCard course={course} />
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
};

export default CourseListPage;
