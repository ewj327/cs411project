import React from 'react';

  
const Search = () => {
  return (
    <div>
        <title>FindRestaurant</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossOrigin="anonymous" />
        <link rel="stylesheet" type="text/css" href="{% static '/css/main.css' %}" />
        <style dangerouslySetInnerHTML={{__html: "\nbody {\n    background-image:url('https://img.freepik.com/premium-photo/food-background-set-dishes-fish-meat-vegetables-black-stone-background-top-view-free-copy-space_187166-16567.jpg?w=1800');\n    background-repeat:no-repeat;\n    background-size:cover;\n}\n" }} />
        <div className="main-search-input-wrap">
          <div className="main-search-input fl-wrap">
            <div className="main-search-input-item">
              <input type="text" defaultValue placeholder="Enter your address" />
            </div>
            <button className="main-search-button">Find Food</button>
          </div>
        </div>
      </div>
  )
};
  
export default Search;