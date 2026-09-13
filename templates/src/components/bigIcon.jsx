import { icon } from "./icons"

export default function BigIcon(props){

    const Icon = icon[props?.icon] 
    return (
<div className="flex w-full items-center justify-center">
            <div
                className="
                    flex
                    h-60 w-60
                    items-center justify-center
                    rounded-2xl
                    bg-gray-800
                    text-gray-100
                    shadow-sm
                    transition-all
                    duration-200
                    hover:-translate-y-0.5
                    hover:bg-gray-700
                    hover:shadow-md
                    sm:h-16 sm:w-16
                    sm:rounded-2xl
                    m-11
                "
            >
                <Icon
                    className="
                        h-6 w-6
                        sm:h-7 sm:w-7
                    "
                />
            </div>
        </div>
    )
}
