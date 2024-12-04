import React, { useMemo } from "react";
import CompanyLink from "./CompanyLink";

type Props = {
    companies: []
}
export default function ListCompanies(props: Props) {
    const baseURL = "https://www.mse.mk/"
    console.log(props.companies)

    function listCompanies() {
        const list = []
        for (let i = 0; i < props.companies.length; i++) {
            list.push(<CompanyLink key={props.companies[i][0]} imageSrc={baseURL + props.companies[i][1]} companyName={props.companies[i][2]} />)
        }
        return list
    }

    const listOfCompanies = useMemo(listCompanies, [props.companies])
    return (
        <div>
            {
                listOfCompanies
            }
        </div>
    )
}
