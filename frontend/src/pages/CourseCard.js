import React from 'react';
import { FaFile, FaStar } from 'react-icons/fa';
import { FaUserGroup } from 'react-icons/fa6';
import Tilt from 'react-parallax-tilt';

// Define PropTypes for runtime type checking
import PropTypes from 'prop-types';

const CourseCard = ({ course }) => {
  return (
    <Tilt>
      <div className='bg-white rounded-lg overflow-hidden cursor-pointer'>
        <div>
          <img src={course.image} alt={course.title} className='w-full h-full object-cover' />
        </div>
        <div className='p-4'>
          <h1 className='ml-auto relative z-[10] h-20 w-20 flex items-center text-lg font-bold justify-center flex-col mt-[-4rem] rounded-full bg-rose-700 text-white'>
            ${course.price}
          </h1>
          <div className='flex items-center mt-6 space-x-4'>
            <span className='text-lg text-black text-opacity-70 font-bold'>{course.category}</span>
            <span className='text-base text-gray-600'>{course.author}</span>
          </div>
          <h1 className='text-xl text-black font-bold mt-2'>{course.title}</h1>
          <div className='flex mt-2 items-center space-x-2'>
            <div className='flex items-center'>
              {[...Array(5)].map((_, index) => (
                <FaStar key={index} className='w-4 h-4 text-yellow-600' />
              ))}
            </div>
            <span className='text-base text-orange-800 font-semibold'>({course.reviewNumber} Reviews)</span>
          </div>
          <div className='mt-6 mb-6 w-full h-[2px] bg-gray-500 opacity-15'></div>
          <div className='flex mb-8 items-center justify-between'>
            <div className='flex items-center space-x-2'>
              <FaFile className='w-4 h-4 text-orange-600' />
              <p className='text-base font-semibold text-gray-800'>{course.lessons} Lessons</p>
            </div>
            <div className='flex items-center space-x-2'>
              <FaUserGroup className='w-4 h-4 text-orange-600' />
              <p className='text-base font-semibold text-gray-800'>{course.students} Students</p>
            </div>
          </div>
        </div>
      </div>
    </Tilt>
  );
};

// PropTypes for runtime type checking
CourseCard.propTypes = {
  course: PropTypes.shape({
    id: PropTypes.number.isRequired,
    image: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    author: PropTypes.string.isRequired,
    reviewNumber: PropTypes.number.isRequired,
    lessons: PropTypes.number.isRequired,
    students: PropTypes.number.isRequired,
    category: PropTypes.string.isRequired,
  }).isRequired,
};

export default CourseCard;
