import { StaticImageData } from "next/image"

export type Company = {
    imageSrc: string,
    companyName: string,
}

type Info = {
    adress: string,
    city: string,
    country: string,
    email: string,
    website: string,
    contactPerson: string,
    prospect: string
}
