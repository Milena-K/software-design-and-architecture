import React from "react";
import Search from "./Search"
import ListCompanies from "./ListCompanies"

export default function Menu() {
  return (
      <div dir="ltr" className="bg-beige h-full w-1/3 rounded-s-lg border border-brown p-5">
        <div className="w-full">
          <Search />
          <div className="mt-5">
            <ListCompanies />
          </div>
        </div>
      </div>
  )
}
