import React from "react";
import BasicInfo from "./BasicInfo";
import InfoButtons from "./InfoButtons";


export default function MainPage() {
  const info = [
    "бул. Александар Македонски бр.12",
    "Скопје",
    "Македонија",
    "alkaloid@alkaloid.com.mk",
    "http://www.alkaloid.com.mk",
    "Виктор Стојчевски \
    Телефон \
    +389 2 3 104 007 \
    Факс \
    +389 2 3 104 081",
    "https://www.mse.mk/Repository/Catalogues/MK/65bff55c-e5dd-478e-a593-344818e54a13.pdf"
  ]

  return (
    <div className="flex gap-5 m-5">
        <div className="w-1/2">
          <BasicInfo info={info} />
        </div>
        <div className="w-1/2">
          <InfoButtons />
        </div>
    </div>
  )
}
