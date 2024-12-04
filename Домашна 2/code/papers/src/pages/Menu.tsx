import React, { useEffect, useState } from "react";
import Search from "./Search"
import ListCompanies from "./ListCompanies"
import axios from 'axios';

export default function Menu() {
    const [companies, setCompanies] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
      axios.get('http://127.0.0.1:5005/companies-10')
           .then(response => {setCompanies(response.data); console.log(response.data)})
        .catch(error => setError(error.message));
    }, []);

    return (
        <div dir="ltr" className="bg-beige h-full w-1/3 rounded-s-lg border border-brown p-5 overflow-scroll">
          <div className="w-full">
            <Search />
            <div className="mt-5">
              {
                companies ? <ListCompanies companies={companies}/> : <p>there was an error</p>
              }
            </div>
          </div>
        </div>
    )
}
