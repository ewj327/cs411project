import kidseg from './kidney_segment.jpg';

const Home = () => {
    return (
        <div className="home">
            <img src={kidseg} alt="kidney_segment" />
            <h2>Smartphone image analysis for real time adequacy assessment during kidney biopsy.</h2>
        </div>
    );
}
 
export default Home;