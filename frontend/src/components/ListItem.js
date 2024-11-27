import React from 'react';
import './ListItem.css'; // Make sure to create and use a CSS file for styling

const ListItem = ({ course }) => {
  return (
    <div className="list-item">
      <img src={course.ImageUrl || "https://via.placeholder.com/200x150"} alt={course.CourseName} className="course-image" />
      <h2 className="course-name">{course.CourseName}</h2>
    </div>
  );
}

export default ListItem;
