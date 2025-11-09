import React from 'react';
import './Info.css';

export default function Info() {
  return (
    <div className="info-container">
      <header className="info-header">
        <h1>SpaceWaze: Advanced Space Navigation</h1>
        <div className="project-description">
          <p>
            SpaceWaze is an innovative project that leverages cutting-edge software engineering 
            principles to compute optimal trajectories for space navigation. Our platform 
            integrates sophisticated algorithms to determine the most efficient paths to 
            celestial destinations.
          </p>
          
          <div className="tech-stack">
            <h2>Technology Architecture</h2>
            <div className="tech-grid">
              <div className="tech-category">
                <h3>Frontend</h3>
                <ul>
                  <li>React - Modern UI framework</li>
                  <li>Node.js - Runtime environment</li>
                </ul>
              </div>
              <div className="tech-category">
                <h3>Backend & Data</h3>
                <ul>
                  <li>Flask - Python web framework</li>
                  <li>MongoDB - NoSQL database</li>
                </ul>
              </div>
              <div className="tech-category">
                <h3>Core Computation</h3>
                <ul>
                  <li>Python - Scientific computing & algorithms</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="mission-statement">
            <h2>Our Mission</h2>
            <p>
              By combining robust full-stack development with advanced computational mathematics, 
              SpaceWaze delivers precise orbital mechanics solutions for space agencies, 
              research institutions, and commercial space ventures.
            </p>
          </div>
        </div>
      </header>
    </div>
  );
}
