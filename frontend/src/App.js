import {
  BrowserRouter as Router,
  Route,
  Routes,
  Link, // Import Link component
} from "react-router-dom";

import './App.css';
import Header from './components/Header';
import CourseListPage from './pages/CourseListPage';
import CoursePage from './pages/CoursePage';

function App() {
  return (
    <div className="App">
      <Header />
      <Router>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<CourseListPage />} />
          <Route path="/course/:id" element={<CoursePage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
