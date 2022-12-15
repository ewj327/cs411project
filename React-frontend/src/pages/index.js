import React from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Link} from 'react-router-dom';


const divStyle = {
  display: 'flex',
  alignItems: 'center'
};

const Home = () => {
  return (
    <div style={divStyle}>
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8M3x8fGVufDB8fHx8&auto=format&fit=crop&w=900&q=60" />
      <Card.Body>
        <Card.Title>Quick Start</Card.Title>
        <Card.Text>
          Hungry? No problem we got you! Enter your address and see the top rating restaurants nearby.  
        </Card.Text>
        <Link to="/search">
        <Button variant="primary">Search restaurants</Button>
        </Link>
      </Card.Body>
    </Card>
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="https://agentestudio.com/uploads/post/image/90/main_user-profile-design.png" />
      <Card.Body>
        <Card.Title>My Profile</Card.Title>
        <Card.Text>
        Add, change, or edit your profile (login needed).
        </Card.Text>
        <Link to="/profile">
        <Button variant="primary">Go to my Profile</Button>
        </Link>
      </Card.Body>
    </Card>
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="https://blog.planview.com/wp-content/uploads/2019/01/10-Point-Checklist-for-Better-Project-Estimates.jpg" />
      <Card.Body>
        <Card.Title>My Wishlist</Card.Title>
        <Card.Text>
        Add your favorite restaurants in wishlist and come back for more next time!
        </Card.Text>
        <Link to="/wishlist">
        <Button variant="primary">Go to my Wishlist</Button>
        </Link>
      </Card.Body>
    </Card>
    </div>
  );
};
  
export default Home;