import BigIcon from './bigIcon'

export default function Detail() {
    return (
        <section
            className="
                w-full
                rounded-3xl
                border border-gray-200
                bg-white
                p-6 sm:p-8
                shadow-[0_4px_30px_rgba(0,0,0,0.04)]
            "
        >
            {/* Header */}
            <div className="flex items-start gap-4">

                <div>
                    <BigIcon icon="image" />
                </div>

                <div className="min-w-0">
                    <h1
                        className="
                            text-xl font-bold
                            tracking-tight
                            text-gray-900
                            sm:text-2xl
                        "
                    >
                        Image Compression API
                    </h1>

                    <p className="mt-1 text-sm text-gray-500">
                        Fast and reliable image compression
                    </p>
                </div>

            </div>


            {/* Description */}
            <div className="mt-7">
                <h2 className="text-sm font-semibold text-gray-900">
                    About this API
                </h2>

                <p
                    className="
                        mt-2
                        text-sm
                        leading-7
                        text-gray-600
                    "
                >
                    Compress and optimize your images with a simple
                    REST API. Reduce file size while maintaining
                    excellent image quality.
                </p>
            </div>


            {/* Supported formats */}
            <div className="mt-7">

                <h2 className="text-sm font-semibold text-gray-900">
                    Supported formats
                </h2>

                <div className="mt-3 flex flex-wrap gap-2">

                    {["JPEG", "PNG", "WebP", "AVIF"].map((format) => (
                        <span
                            key={format}
                            className="
                                rounded-lg
                                border border-gray-200
                                bg-gray-50
                                px-3 py-1.5
                                text-xs font-medium
                                text-gray-600
                            "
                        >
                            {format}
                        </span>
                    ))}

                </div>
            </div>


            {/* Endpoint */}
            <div className="mt-7">

                <h2 className="text-sm font-semibold text-gray-900">
                    Endpoint
                </h2>

                <div
                    className="
                        mt-3
                        flex items-center
                        overflow-x-auto
                        rounded-xl
                        bg-gray-950
                        px-4 py-3
                    "
                >
                    <span className="mr-3 text-xs font-bold text-green-400">
                        POST
                    </span>

                    <code className="whitespace-nowrap text-xs text-gray-300">
                        /api/v1/image/compress
                    </code>
                </div>

            </div>


            {/* Footer info */}
            <div
                className="
                    mt-7
                    flex flex-wrap
                    gap-x-6 gap-y-3
                    border-t border-gray-100
                    pt-5
                "
            >
                <div>
                    <span className="block text-xs text-gray-400">
                        Authentication
                    </span>

                    <span className="mt-1 block text-sm font-medium text-gray-700">
                        API Key
                    </span>
                </div>

                <div>
                    <span className="block text-xs text-gray-400">
                        Response
                    </span>

                    <span className="mt-1 block text-sm font-medium text-gray-700">
                        JSON
                    </span>
                </div>

                <div>
                    <span className="block text-xs text-gray-400">
                        Method
                    </span>

                    <span className="mt-1 block text-sm font-medium text-gray-700">
                        POST
                    </span>
                </div>
            </div>

        </section>
    );
}