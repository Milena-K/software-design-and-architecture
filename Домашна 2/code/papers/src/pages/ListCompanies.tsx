import React, { useMemo } from "react";
import CompanyLink from "./CompanyLink";
import alkaloid from "../../public/65bff55c-e5dd-478e-a593-344818e54a13.jpg"
import Company from "../types"
import { StaticImageData } from "next/image";

export default function ListCompanies() {
    const companies: Map<string, StaticImageData> = {
        "Алкалоид АД Скопје 1": alkaloid,
        "Алкалоид АД Скопје 2": alkaloid,
        "Алкалоид АД Скопје 3": alkaloid,
    }

    function listCompanies() {
        const list = []
        for ( const [companyName, companyImg] of Object.entries(companies) ) {
            list.push(<CompanyLink key={companyName} imageSrc={companyImg} companyName={companyName} />)
        }
        return list
    }

    const listOfCompanies = useMemo(listCompanies, [companies])
    return (
        <div>
            {
                listOfCompanies
            }
        </div>
    )
}
