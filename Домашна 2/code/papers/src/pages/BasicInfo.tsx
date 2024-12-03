import React from "react";

type Props = JSX.IntrinsicElements['div'];
interface DivProps extends Props {
  info: string[];
}


export default function BasicInfo(props: DivProps) {
    const fields = [ "Адресa", "Град", "Државa", "e-mail адреса", "Веб страница", "Лице за контакт"]
    return (
        <div className="bg-green rounded-lg">
            <div className="text-blue grid grid-cols-1 grid-rows-7 text-wrap fit p-5 gap-2">
                <p className="mt-5 h-fit">Основни податоци за издавачот</p>
                {
                    fields.map((field, ind) => (
                        <div key={ind}>
                            <p>{field}</p>
                            <p>{props.info[ind]}</p>
                        </div>
                    ))
                }
                <div className="mt-2">
                    <p>Проспект</p>
                    <a href={props.info[8]}>Преземи Проспект</a>
                </div>
            </div>
        </div>
    )
}
