// CoursePage.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './CoursePage.css';
import CaesarCipherGame from '../games/CaesarCipherGame';
import SteganographyGame from '../games/SteganographyGame';
import BruteForceLogin from '../games/BruteForceLogin';
import SqlInjectionSimulation from '../games/SqlInjectionSimulation';

function CoursePage() {
  const { id } = useParams();
  const [course, setCourse] = useState({});
  const [activeLesson, setActiveLesson] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/courses/${id}/`)
      .then(response => response.json())
      .then(data => {
        setCourse(data);
      })
      .catch(error => {
        console.error(error);
      });
  }, [id]);

  const toggleLesson = (lesson) => {
    setActiveLesson(activeLesson === lesson ? null : lesson);
  };

  return (
    <div>
      <h1>{course.CourseName}</h1>
      <p>{course.Description}</p>
      <p>Start Date: {course.StartDate}</p>
      <p>End Date: {course.EndDate}</p>

      <div className="container">
        {course.lessons && course.lessons.length > 0 ? (
          course.lessons.map((lesson, index) => (
            <div className="accordion" key={index}>
              <div className="accordion-head" onClick={() => toggleLesson(lesson)}>
                <p>{index + 1}</p>
                <p>{lesson}</p>
                <p><i className="bi bi-list"></i></p>
              </div>
              <div className={`accordion-body ${activeLesson === lesson ? 'open' : 'hidden'}`}>
                <p>Lesson details for {lesson}</p>
                <iframe src="https://www.youtube.com/embed/kPylihJRG70" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
              </div>
            </div>
          ))
        ) : (
          <p>No lessons available.</p>
        )}
      </div>

      {/* Replace the iframe with the Caesar Cipher Game */}
      <div className="container" style={{ display: "flex", alignItems: "center", justifyContent: "center", overflow: "hidden", width: "750px", height: "500px" }}>
        <CaesarCipherGame />
      </div>
      <div className="container" style={{ display: "flex", alignItems: "center", justifyContent: "center", overflow: "hidden", width: "750px", height: "500px" }}>
        <SteganographyGame />
      </div>
      <div className="container" style={{ display: "flex", alignItems: "center", justifyContent: "center", overflow: "hidden", width: "750px", height: "500px" }}>
        <BruteForceLogin />
      </div>
      <div className="container" style={{ display: "flex", alignItems: "center", justifyContent: "center", overflow: "hidden", width: "750px", height: "500px" }}>
        <SqlInjectionSimulation  />
      </div>
    </div>
  );
}

export default CoursePage;
