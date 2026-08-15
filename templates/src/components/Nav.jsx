export default function NavBar() {
    return (
        <nav className="w-full px-6 py-4">
            <div 
            className="max-w-7xl mx-auto flex items-center
             justify-between rounded-2xl bg-gray-800 px-6 py-4 text-white">
                <a href="/" className="text-xl font-bold hover:text-white">
                    باینری API
                </a>

                <div className="flex items-center gap-6">
                    <a href="/">خانه</a>
                </div>
            </div>
        </nav>
    )
}