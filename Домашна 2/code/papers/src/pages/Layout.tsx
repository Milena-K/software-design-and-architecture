import React from "react";
import Menu from "./Menu";
import Link from "next/link";


export default function Layout({ children }) {
  const company_name = "Алкалоид АД Скопје";
  return (
      <div className="bg-green h-screen w-screen flex justify-center align-content-center">
        <div className="w-4/5 h-4/5 flex m-auto">
          <Menu />
        <div dir="rtl" className="bg-beige grow rounded-s-lg border border-brown">
        <div dir="ltr" className="h-full  w-full overflow-scroll">
          <Link href="/">
            <h1 className="text-black text-center m-5 text-xl">
                {company_name}
            </h1>
          </Link>
            {children}
        </div>
        </div>
        </div>
      </div>
  )
}
