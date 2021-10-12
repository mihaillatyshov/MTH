import React from 'react'
import Node from './Node'

const NowNode = ( {node, onNodeChange} ) => {
	return (
		<div className="col-4">
			{
				(typeof node === 'undefined') ? (
					<div>Loading...</div>
				) : (
					<Node node={node} onNodeChange={() => {}}/>
				)
			}
		</div>
	)
}

export default NowNode
