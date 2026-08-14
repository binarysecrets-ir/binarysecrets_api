export default function ApiCard() {
    return (
        <div className="
            group
            min-w-2xs
            max-w-2xl
            rounded-2xl
            bg-white
            p-6
            mx-10
            my-5
            ring-1 ring-gray-200
            transition-all duration-300
            hover:-translate-y-1
            hover:shadow-2xl
        ">

            <div className="
                mb-5
                flex h-12 w-12
                items-center justify-center
                rounded-xl
                bg-gray-900
                text-xl text-white
            ">
                ⚡
            </div>

            <h2 className="text-xl font-semibold text-gray-900">
                Image API
            </h2>

            <p className="mt-2 text-sm leading-6 text-gray-500">
                Compress, optimize and transform your images
                through a simple REST API.
            </p>

            <div className="mt-5 flex items-center gap-2">
                <span className="rounded-full bg-gray-100 px-3 py-1 text-xs font-medium text-gray-600">
                    REST
                </span>

                <span className="rounded-full bg-gray-100 px-3 py-1 text-xs font-medium text-gray-600">
                    JSON
                </span>
            </div>

            <button className="
                mt-6
                flex w-full items-center justify-center
                rounded-xl
                bg-gray-900
                px-4 py-3
                text-sm font-medium text-white
                transition
                hover:bg-gray-800
                group-hover:shadow-md
            ">
                Explore API
                <span className="ml-2 transition-transform group-hover:translate-x-1">
                    →
                </span>
            </button>

        </div>
    );
}