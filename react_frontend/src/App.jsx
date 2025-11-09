import { Navbar, Nav, Container } from "react-bootstrap";
import { Routes, Route, Link } from "react-router-dom";
import Home from "./Home";
import Info from "./Info";
import Project from "./Project";

function App() {
  return (
    <>
      {/* Navbar */}
      <Navbar bg="primary" variant="dark" expand="md" fixed="top">
        <Container>
          <Navbar.Brand as={Link} to="/">
            SpaceWaze
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link as={Link} to="/">
                Home
              </Nav.Link>
              <Nav.Link as={Link} to="/info">
                Info
              </Nav.Link>
              <Nav.Link as={Link} to="/project">
                Pathfinder
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      {/* Page content */}
      <div style={{ paddingTop: "56px", textAlign: "center" }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/info" element={<Info />} />
          <Route path="/project" element={<Project />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
