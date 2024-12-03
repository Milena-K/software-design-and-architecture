import React from "react";

{/* <input placeholder="Search" className="bg-green rounded-lg p-2 placeholder:text-brown ring-2 ring-black"/> */ }
export default function Search() {
  return (
    <input
      className="border bg-beige border-brown placeholder:text-brown rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-brown w-full"
      placeholder="Search"
      type="text"
    />

  )
}
