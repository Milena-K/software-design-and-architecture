import React from "react";
import Image, { StaticImageData } from "next/image"
import Company from "../types"

export default function CompanyLink(props: Company) {
    /* console.log(props) */

    return (
        <div className="flex justify-content text-center align-content my-2">
            <Image width={50} height={50}
                   src={props.imageSrc}
                   alt="Company logo"
                   className="grow min-w-12 w-12 h-12 min-h-12 max-w-12 max-h-12" />
            <p className="ml-5 my-auto h-full text-center text-wrap">{props.companyName}</p>
        </div>
    )
}
