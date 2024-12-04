import React, { useMemo } from "react";

import Link from "next/link";

export default function InfoButtons() {
    const button_map = {
        "Финансиски извештаи": "/Finansiski",
        "Вести": "/Vesti",
        "Објави од берзата": "/Objavi",
        "Податоци": "/Podatoci",
        "Показатели": "/Pokazateli",
        "Дејност": "/Dejnost",
        "Управа": "/Uprava"
    };

    const makeButtons = () => {
        const buttons = []
        for (const [name, link] of Object.entries(button_map)) {
            buttons.push(
                <Link className="text-center" href={link} key={name}>
                    <button className="bg-blue text-white w-3/4 p-2 rounded-lg m-auto">
                        {name}
                    </button>
                </Link>
            )
        }
        return buttons
    }

    const listOfButtons = useMemo(makeButtons, [button_map])
    return (
        <div className="w-full grid grid-rows-7 grid-cols-1 gap-5">
            { listOfButtons }
        </div>
    )
}
